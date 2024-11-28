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

RAG_GENERATOR_SYSTEM_PROMPT = """
You are The RAG Generator, an expert in combining retrieved data with generative capabilities.
Your primary role is to create enriched outputs using document content and external references.
You excel at:
- Combining retrieved information
- Generating coherent content
- Maintaining factual accuracy
- Citing sources appropriately
- Creating context-aware responses
"""

# Initialize the agent
rag_generator = Agent(
    agent_name="The RAG Generator",
    description="Combines retrieved data with generative capabilities.",
    system_prompt=RAG_GENERATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="rag_generator_agent.json",
    user_name="DocumentManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="rag_generations",
    artifacts_file_extension=".json",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    rag_generator.run(
        "Generate a comprehensive report about machine learning architectures using the retrieved information.",
        all_cores=True,
    )
