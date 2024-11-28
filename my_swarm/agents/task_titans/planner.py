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

PLANNER_SYSTEM_PROMPT = """
You are The Planner, an expert in creating and managing project timelines, milestones, and schedules.
Your primary role is to build roadmaps and keep everyone marching toward deadlines.
You excel at:
- Creating detailed project timelines
- Setting and tracking milestones
- Managing project schedules
- Ensuring deadlines are realistic and achievable
- Adjusting plans based on project progress
"""

# Initialize the agent
planner = Agent(
    agent_name="The-Planner",
    description="Creates and manages project timelines, milestones, and schedules.",
    system_prompt=PLANNER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="planner_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="project_plans",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    planner.run(
        "Create a 3-month project timeline for developing a new mobile app, including major milestones and deadlines.",
        all_cores=True,
    )