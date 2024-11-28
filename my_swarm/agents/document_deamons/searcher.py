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

SEARCHER_SYSTEM_PROMPT = """
You are The Searcher, an expert in locating documents quickly based on keywords.
Your primary role is to save time by finding relevant documents effortlessly.
You excel at:
- Keyword-based document search
- Content relevance ranking
- Quick document retrieval
- Search result organization
- Advanced search techniques
"""

# Initialize the agent
searcher = Agent(
    agent_name="The Searcher",
    description="Locates documents quickly based on keywords.",
    system_prompt=SEARCHER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="searcher_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="document_searches",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    searcher.run(
        "Search for documents matching these keywords and rank them by relevance.",
        all_cores=True,
    )
