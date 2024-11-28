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

ARCHIVIST_SYSTEM_PROMPT = """
You are The Archivist, an expert in storing and retrieving documents efficiently.
Your primary role is to maintain a well-organized document archive.
You excel at:
- Organizing document storage
- Creating efficient retrieval systems
- Maintaining document integrity
- Managing storage space
- Implementing archival best practices
"""

# Initialize the agent
archivist = Agent(
    agent_name="The Archivist",
    description="Stores and retrieves documents efficiently.",
    system_prompt=ARCHIVIST_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="archivist_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_archives",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    archivist.run(
        "Archive these documents according to the storage policy and ensure efficient retrieval.",
        all_cores=True,
    )
