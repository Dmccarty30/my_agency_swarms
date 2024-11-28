import os
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from swarms import Agent
from swarm_models import OpenAIChat
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Initialize our models
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
model = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4-o1-mini",
    temperature=0.1
)

# Pydantic models for structured data
class Task(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    subtasks: List[Dict] = Field(default_factory=list)
    estimated_duration: str
    dependencies: List[str] = Field(default_factory=list)
    can_parallel: bool = True
    status: str = "pending"
    assigned_to: Optional[str] = None
    
class ProjectStatus(BaseModel):
    project_id: str
    title: str
    completed_tasks: List[str] = Field(default_factory=list)
    in_progress: List[str] = Field(default_factory=list)
    blocked: List[str] = Field(default_factory=list)
    agent_statuses: Dict[str, Dict] = Field(default_factory=dict)

def task_breakdown_tool(task: str) -> Dict:
    """Breaks down complex tasks into manageable subtasks with timelines"""
    prompt = f"""
    Analyze this task and break it down into:
    1. Clear subtasks with dependencies
    2. Time estimates for each component
    3. Parallel processing opportunities
    4. Required resources
    
    Task: {task}
    
    Return as structured JSON.
    """
    
    response = model(prompt)
    return response

def progress_monitor_tool(project_id: str, tasks: List[Task]) -> ProjectStatus:
    """Monitors and reports on task and project progress"""
    prompt = f"""
    Analyze the current project state and provide:
    1. Task completion status
    2. Blockers and dependencies
    3. Resource allocation status
    4. Timeline adherence
    
    Project ID: {project_id}
    Tasks: {tasks}
    
    Return as structured JSON.
    """
    
    response = model(prompt)
    return ProjectStatus(**response)

class PlannerAgent(Agent):
    def __init__(
        self,
        name: str = "The Planner",
        description: str = "Task Titan specialized in project planning and management",
        system_prompt: str = """You are The Planner, a specialized Task Titan agent designed to:
1. Create and manage project timelines with precision
2. Handle milestone tracking and schedule management
3. Build comprehensive roadmaps for project success
4. Keep teams aligned and moving toward deadlines
5. Optimize resource allocation and parallel processing

Your responses should always be in JSON format with the following structure:
{
    "analysis": "Your understanding of the task",
    "plan": {
        "tasks": [...],
        "timeline": {...},
        "dependencies": [...],
        "parallel_tracks": [...]
    },
    "next_steps": [...],
    "risks": [...],
    "recommendations": [...]
}""",
        max_loops: int = 5
    ):
        super().__init__(
            agent_name=name,
            description=description,
            system_prompt=system_prompt,
            llm=model,
            max_loops=max_loops,
            dashboard=True,
            verbose=True,
            streaming_on=True,
            dynamic_temperature_enabled=True,
            output_type="json"
        )
        
        # Initialize Pinecone index
        self.index_name = "planner-titan-index"
        
        # Check if index exists, if not create it
        existing_indexes = [index.name for index in pc.list_indexes()]
        
        if self.index_name not in existing_indexes:
            pc.create_index(
                name=self.index_name,
                dimension=1536,  # OpenAI embeddings dimension
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-west-2"
                )
            )
        
        # Get the index
        self.index = pc.Index(self.index_name)
        
        # Register tools
        self.tools = [
            task_breakdown_tool,
            progress_monitor_tool
        ]
        
        # Initialize tracking
        self.current_project_id = None
        self.active_tasks = []
        
    async def run(self, task: str, *args, **kwargs) -> Dict:
        """
        Enhanced run method that processes tasks with parallel capability
        """
        try:
            # Generate project ID if needed
            if not self.current_project_id:
                self.current_project_id = str(uuid.uuid4())
            
            # Break down the task
            task_breakdown = task_breakdown_tool(task)
            
            # Store in vector memory
            self._store_in_memory(task, task_breakdown)
            
            # Process tasks
            parallel_tasks = [t for t in task_breakdown["tasks"] if t["can_parallel"]]
            sequential_tasks = [t for t in task_breakdown["tasks"] if not t["can_parallel"]]
            
            # Execute tasks based on their type
            results = {
                'parallel_tasks': await self._execute_parallel_tasks(parallel_tasks),
                'sequential_tasks': await self._execute_sequential_tasks(sequential_tasks)
            }
            
            # Monitor progress
            status = progress_monitor_tool(
                self.current_project_id,
                self.active_tasks
            )
            
            # Return formatted response
            return {
                "project_id": self.current_project_id,
                "task_breakdown": task_breakdown,
                "execution_results": results,
                "project_status": status.dict(),
                "next_steps": self._generate_next_steps(status)
            }
            
        except Exception as e:
            self.logger.error(f"Error in PlannerAgent execution: {str(e)}")
            raise
            
    def _store_in_memory(self, task: str, breakdown: Dict):
        """Store task data in Pinecone"""
        # Get embeddings from OpenAI
        response = self.llm.embeddings.create(input=str(breakdown))
        vector = response.data[0].embedding
        
        # Store in Pinecone
        self.index.upsert(
            vectors=[(task, vector, breakdown)],
            namespace="task_patterns"
        )
    
    async def _execute_parallel_tasks(self, tasks: List[Dict]) -> List[Dict]:
        """Execute tasks that can run in parallel"""
        return await self._process_tasks(tasks, parallel=True)
    
    async def _execute_sequential_tasks(self, tasks: List[Dict]) -> List[Dict]:
        """Execute tasks that must run sequentially"""
        return await self._process_tasks(tasks, parallel=False)
    
    def _generate_next_steps(self, status: ProjectStatus) -> List[str]:
        """Generate next actions based on current project status"""
        prompt = f"""
        Based on the current project status:
        {status}
        
        Generate a prioritized list of next steps to keep the project on track.
        Return as a JSON array of strings.
        """
        
        response = self.llm(prompt)
        return response

# Example usage
if __name__ == "__main__":
    planner = PlannerAgent()
    result = planner.run("Create a comprehensive plan for building out all agents in agent_convo.md")
    print(result)