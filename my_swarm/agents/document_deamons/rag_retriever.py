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

RAG_RETRIEVER_SYSTEM_PROMPT = """
You are The RAG Retriever, an expert in searching databases for relevant content.
Your primary role is to provide up-to-date information for document-related tasks.
You excel at:
- Searching through document databases
- Finding relevant context
- Retrieving accurate information
- Ranking search results
- Maintaining search efficiency
"""

# Initialize the agent
rag_retriever = Agent(
    agent_name="The RAG Retriever",
    description="Searches databases for relevant content.",
    system_prompt=RAG_RETRIEVER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="rag_retriever_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="rag_retrievals",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    rag_retriever.run(
        "Search the database for relevant information about machine learning architectures.",
        all_cores=True,
    )
