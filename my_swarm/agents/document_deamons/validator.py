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

VALIDATOR_SYSTEM_PROMPT = """
You are The Validator, an expert in checking documents for errors and inconsistencies.
Your primary role is to guarantee accuracy and adherence to standards.
You excel at:
- Identifying errors and inconsistencies
- Checking against style guides
- Validating document formatting
- Ensuring data accuracy
- Maintaining quality standards
"""

# Initialize the agent
validator = Agent(
    agent_name="The Validator",
    description="Checks documents for errors and inconsistencies.",
    system_prompt=VALIDATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="validator_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_validations",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    validator.run(
        "Check this document for errors, inconsistencies, and compliance with standards.",
        all_cores=True,
    )
