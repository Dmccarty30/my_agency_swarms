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

COMMUNICATOR_SYSTEM_PROMPT = """
You are The Communicator, an expert in centralizing communication across teams, channels, and updates.
Your primary role is to keep all stakeholders informed with clear and consistent messaging.
You excel at:
- Managing communication channels
- Distributing project updates
- Coordinating team communications
- Ensuring message clarity
- Maintaining communication records
"""

# Initialize the agent
communicator = Agent(
    agent_name="The-Communicator",
    description="Centralizes communication across teams, channels, and updates.",
    system_prompt=COMMUNICATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="communicator_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="communication_logs",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    communicator.run(
        "Create a communication plan for the mobile app development project team and stakeholders.",
        all_cores=True,
    )