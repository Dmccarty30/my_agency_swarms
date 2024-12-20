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
    model_name="gpt-4o-mini", 
    temperature=0.1
)

# Initialize the agent
agent = Agent(
    agent_name="The Correspondent",
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="the_correspondent.json",
    user_name="SweetP",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",  # "json", "dict", "csv" OR "string" soon "yaml" and
    auto_generate_prompt=False,  # Auto generate prompt for the agent based on name, description, and system prompt, task
    artifacts_on=True,
    artifacts_output_path="",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)


agent.run(
    "How can I establish a ROTH IRA to buy stocks and get a tax break? What are the criteria. Create a report on this question.",
    all_cores=True,
)
