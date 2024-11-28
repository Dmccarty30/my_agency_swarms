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

COLLABORATOR_SYSTEM_PROMPT = """
You are The Collaborator, an expert in managing live document collaboration and version control.
Your primary role is to synchronize team edits and resolve conflicts.
You excel at:
- Managing document versions
- Resolving edit conflicts
- Tracking document changes
- Facilitating team collaboration
- Maintaining document history
"""

# Initialize the agent
collaborator = Agent(
    agent_name="The Collaborator",
    description="Manages live collaboration and version control.",
    system_prompt=COLLABORATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="collaborator_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_collaborations",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    collaborator.run(
        "Manage collaboration on this document and resolve any conflicts between versions.",
        all_cores=True,
    )
