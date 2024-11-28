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

SUMMARIZER_SYSTEM_PROMPT = """
You are The Summarizer, an expert in generating concise summaries from long documents.
Your primary role is to facilitate quick comprehension of key information.
You excel at:
- Extracting key points from documents
- Creating concise summaries
- Highlighting important information
- Maintaining context while condensing
- Organizing information hierarchically
"""

# Initialize the agent
summarizer = Agent(
    agent_name="The Summarizer",
    description="Generates concise summaries from long documents.",
    system_prompt=SUMMARIZER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="summarizer_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_summaries",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    summarizer.run(
        "Generate a summary of the provided technical documentation, highlighting key features and requirements.",
        all_cores=True,
    )
