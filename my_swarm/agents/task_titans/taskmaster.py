import os
from dotenv import load_dotenv
from swarm_models import OpenAIChat
from swarms import Agent

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    openai_api_key=api_key, 
    model_name="gpt-4-mini", 
    temperature=0.1
)

TASKMASTER_SYSTEM_PROMPT = """
You are The TaskMaster, an expert in assigning, tracking, and monitoring tasks across team members or systems.
Your primary role is to ensure everyone knows their role and deadlines are met.
You excel at:
- Assigning tasks to appropriate team members
- Tracking task progress and completion
- Setting and monitoring deadlines
- Managing task dependencies
- Providing status updates and reports
"""

# Initialize the agent
taskmaster = Agent(
    agent_name="The-TaskMaster",
    description="Assigns, tracks, and monitors tasks across team members or systems.",
    system_prompt=TASKMASTER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="taskmaster_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="task_assignments",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    taskmaster.run(
        "Create task assignments for the mobile app development team, including deadlines and dependencies.",
        all_cores=True,
    )