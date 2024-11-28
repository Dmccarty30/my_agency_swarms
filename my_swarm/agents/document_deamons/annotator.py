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

ANNOTATOR_SYSTEM_PROMPT = """
You are The Annotator, an expert in adding insightful notes and highlights to documents.
Your primary role is to enhance understanding and provide valuable insights.
You excel at:
- Adding contextual notes to documents
- Highlighting key information
- Creating meaningful annotations
- Providing cross-references
- Identifying important concepts
"""

# Initialize the agent
annotator = Agent(
    agent_name="The Annotator",
    description="Adds notes and highlights to documents for review.",
    system_prompt=ANNOTATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="annotator_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_annotations",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    annotator.run(
        "Review this document and add relevant annotations and highlights to improve understanding.",
        all_cores=True,
    )
