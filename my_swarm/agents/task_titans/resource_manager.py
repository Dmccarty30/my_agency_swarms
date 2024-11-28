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

RESOURCE_MANAGER_SYSTEM_PROMPT = """
You are The Resource Manager, an expert in efficiently allocating resources (people, tools, or time).
Your primary role is to avoid burnout and bottlenecks by ensuring optimal resource utilization.
You excel at:
- Allocating resources efficiently
- Managing resource availability
- Optimizing resource usage
- Tracking resource utilization
- Preventing resource conflicts
"""

# Initialize the agent
resource_manager = Agent(
    agent_name="The-Resource-Manager",
    description="Efficiently allocates resources (people, tools, or time).",
    system_prompt=RESOURCE_MANAGER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="resource_manager_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="resource_allocations",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    resource_manager.run(
        "Create a resource allocation plan for the mobile app development project team and tools.",
        all_cores=True,
    )