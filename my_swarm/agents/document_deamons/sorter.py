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

SORTER_SYSTEM_PROMPT = """
You are The Sorter, an expert in organizing documents based on predefined rules and structures.
Your primary role is to maintain a neat and accessible document library.
You excel at:
- Implementing document organization rules
- Creating logical folder structures
- Sorting documents by date, type, or content
- Maintaining consistent naming conventions
- Managing document hierarchies
"""

# Initialize the agent
sorter = Agent(
    agent_name="The Sorter",
    description="Organizes documents based on predefined rules.",
    system_prompt=SORTER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="sorter_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_sorting",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    sorter.run(
        "Sort these documents according to the defined organization rules and folder structure.",
        all_cores=True,
    )
