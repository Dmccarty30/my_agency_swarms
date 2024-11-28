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

EXTRACTOR_SYSTEM_PROMPT = """
You are The Extractor, an expert in pulling specific information from documents.
Your primary role is to isolate critical details for further use.
You excel at:
- Identifying key information in documents
- Extracting specific data points
- Organizing extracted information
- Maintaining data accuracy
- Creating structured outputs
"""

# Initialize the agent
extractor = Agent(
    agent_name="The Extractor",
    description="Pulls specific information from documents.",
    system_prompt=EXTRACTOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="extractor_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_extractions",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    extractor.run(
        "Extract key information from this document according to the specified criteria.",
        all_cores=True,
    )
