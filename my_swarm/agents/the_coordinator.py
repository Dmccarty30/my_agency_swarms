import os
from typing import List, Dict, Any, Optional
from datetime import datetime
from dotenv import load_dotenv
from swarm_models import OpenAIChat
from swarms import Agent
from swarms.tools.base_tool import BaseTool

# Load environment variables
load_dotenv()

def research_tool(query: str) -> str:
    """Research tool for gathering information on specific topics"""
    return f"Researching information about: {query}"

def analysis_tool(data: str) -> str:
    """Analysis tool for processing and interpreting data"""
    return f"Analyzing data: {data}"

def task_delegation_tool(task: str, agent: str) -> str:
    """Tool for delegating tasks to specific agents"""
    return f"Delegating task: {task} to agent: {agent}"

# List of tools available to the Coordinator
coordinator_tools = [
    research_tool,
    analysis_tool,
    task_delegation_tool
]

# Define standard operating procedures for the Coordinator
coordinator_sop = """
Standard Operating Procedures for Coordinator Agent:

1. Query Analysis
   - Parse incoming user queries
   - Identify key requirements and objectives
   - Determine scope and complexity

2. Planning Phase
   - Break down complex tasks into subtasks
   - Identify required resources and agents
   - Create execution timeline

3. Task Delegation
   - Match tasks with appropriate agents
   - Provide clear instructions and context
   - Set performance expectations

4. Monitoring and Control
   - Track task progress
   - Identify and address bottlenecks
   - Ensure quality standards

5. Feedback and Optimization
   - Collect performance metrics
   - Provide constructive feedback
   - Implement process improvements
"""

# Create an instance of the OpenAIChat class with enhanced parameters
model = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4-1106-preview",
    temperature=0.1,
    max_tokens=4096,
    top_p=0.95,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

# Initialize the Coordinator Agent with comprehensive configuration
coordinator = Agent(
    name="The Coordinator",
    description="""The Coordinator is the central orchestrating agent responsible for managing and optimizing the agent swarm. 
    It excels in task decomposition, resource allocation, and ensuring efficient collaboration between various specialized agents.""",
    system_prompt="""You are the Coordinator, a sophisticated orchestration agent designed to manage a swarm of specialized AI agents.
    Your core responsibilities include:
    
    1. Strategic Planning: Develop comprehensive strategies for complex tasks
    2. Resource Management: Optimize agent allocation and utilization
    3. Quality Control: Ensure deliverables meet or exceed expectations
    4. Risk Management: Identify and mitigate potential issues
    5. Performance Optimization: Continuously improve swarm efficiency
    
    Approach each task with analytical precision and maintain clear communication with all stakeholders.""",
    
    # Core Configuration
    llm=model,
    max_loops=5,
    loop_interval=1,
    retry_attempts=3,
    retry_interval=1,
    
    # Memory and Context
    context_length=16384,
    memory_chunk_size=4000,
    
    # Tool Configuration
    tools=coordinator_tools,
    tool_choice="auto",
    execute_tool=True,
    tool_system_prompt="Use tools strategically to accomplish complex tasks",
    
    # Operational Settings
    autosave=True,
    dashboard=True,
    verbose=True,
    interactive=True,
    streaming_on=True,
    
    # Memory and State Management
    saved_state_path="coordinator_state.json",
    long_term_memory=None,  # Can be configured with a vector database
    
    # Temperature Control
    dynamic_temperature_enabled=True,
    temperature=0.1,
    
    # Processing Configuration
    output_type="json",
    function_calling_type="json",
    metadata_output_type="json",
    
    # Standard Operating Procedures
    sop=coordinator_sop,
    
    # Advanced Features
    chain_of_thoughts=True,
    algorithm_of_thoughts=True,
    tree_of_thoughts=True,
    
    # Performance and Resource Management
    max_tokens=8000,
    timeout=300,
    
    # Artifact Management
    artifacts_on=True,
    artifacts_output_path="coordinator_artifacts",
    artifacts_file_extension=".md",
    
    # Device Configuration
    device="cpu",
    all_cores=True,
    
    # Additional Features
    auto_generate_prompt=True,
    rag_every_loop=True,
    plan_enabled=True,
    
    # Custom Settings
    user_name="User",
    custom_exit_command="exit_coordinator",
    return_history=True,
    return_step_meta=True,
    print_every_step=True
)

# Example usage functions
def handle_task_delegation(task: str, available_agents: List[str]) -> Dict[str, str]:
    """Handle task delegation to available agents"""
    return coordinator.run(
        f"Delegate the following task: {task} to these available agents: {', '.join(available_agents)}"
    )

def generate_task_plan(task: str) -> Dict[str, Any]:
    """Generate a comprehensive plan for a given task"""
    return coordinator.run(
        f"Create a detailed plan for the following task: {task}"
    )

def monitor_task_progress(task_id: str) -> Dict[str, Any]:
    """Monitor the progress of a specific task"""
    return coordinator.run(
        f"Check the progress of task {task_id} and provide a status report"
    )

if __name__ == "__main__":
    # Example usage
    task = """
    Analyze the current market conditions for cryptocurrency investments, 
    considering technical indicators, market sentiment, and regulatory environment. 
    Provide a comprehensive report with investment recommendations.
    """
    
    # Run the coordinator with specific schedule and device configuration
    result = coordinator.run(
        task=task,
        device="cpu",
        all_cores=True,
        scheduled_run_date=datetime.now(),
        do_not_use_cluster_ops=False
    )
    
    # Print the results
    print("Task Execution Results:", result)