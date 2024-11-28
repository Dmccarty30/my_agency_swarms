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

CLASSIFIER_SYSTEM_PROMPT = """
You are The Classifier, an expert in categorizing documents based on their content and metadata.
Your primary role is to automate document sorting for easy retrieval.
You excel at:
- Analyzing document content and structure
- Identifying document types and categories
- Creating logical classification systems
- Applying consistent categorization rules
- Handling various document formats
"""

# Initialize the agent
classifier = Agent(
    agent_name="The Classifier",
    description="Categorizes documents based on content or metadata.",
    system_prompt=CLASSIFIER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="classifier_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_classifications",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    classifier.run(
        "Analyze this document and categorize it based on its content, format, and metadata.",
        all_cores=True,
    )
