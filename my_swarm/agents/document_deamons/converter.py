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

CONVERTER_SYSTEM_PROMPT = """
You are The Converter, an expert in transforming documents between different formats.
Your primary role is to ensure document compatibility and usability.
You excel at:
- Converting between document formats
- Preserving document formatting
- Maintaining data integrity
- Handling batch conversions
- Supporting various file types
"""

# Initialize the agent
converter = Agent(
    agent_name="The Converter",
    description="Transforms documents between formats.",
    system_prompt=CONVERTER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="converter_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_conversions",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    converter.run(
        "Convert this document to the specified format while preserving its structure and content.",
        all_cores=True,
    )
