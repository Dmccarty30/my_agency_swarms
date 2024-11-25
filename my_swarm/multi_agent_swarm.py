import os
from dotenv import load_dotenv
from swarms import Agent, SequentialWorkflow
from swarm_models import OpenAIChat
from loguru import logger

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAIChat model
model = OpenAIChat(
    openai_api_key=api_key,
    model_name="gpt-4o-mini",
    temperature=0.1,
)

# Initialize logging
logger.add("multi_agent_swarm.log", rotation="1 MB")

# Define Specialized Agents

# Researcher Agent
researcher_agent = Agent(
    agent_name="Researcher",
    agent_description="Searches the internet for relevant information on specified topics.",
    system_prompt="""
    You are a Researcher Agent. 
    Task: Search the internet for the most recent and relevant information on the given topic.
    Provide a summary of findings with sources.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="researcher_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="string",
)

# Scraper Agent
scraper_agent = Agent(
    agent_name="Scraper",
    agent_description="Extracts data from identified web sources accurately.",
    system_prompt="""
    You are a Scraper Agent.
    Task: Extract structured data from the provided web sources.
    Ensure accuracy and completeness in data extraction.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="scraper_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="string",
)

# Parser Agent
parser_agent = Agent(
    agent_name="Parser",
    agent_description="Processes and structures the scraped data for analysis.",
    system_prompt="""
    You are a Parser Agent.
    Task: Process the scraped data and structure it into a coherent and analyzable format.
    Ensure that the data is clean and well-organized.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="parser_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="string",
)

# Composer Agent
composer_agent = Agent(
    agent_name="Composer",
    agent_description="Synthesizes the processed data into comprehensive papers.",
    system_prompt="""
    You are a Composer Agent.
    Task: Compose a comprehensive paper based on the structured data provided.
    Ensure clarity, coherence, and proper formatting in the final document.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="composer_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="string",
)

# Initialize the Swarm Router with the defined agents
swarm_router = SequentialWorkflow(
    name="Research-Paper-Composition-Swarm",
    description="A swarm of agents collaborating to research, scrape, parse, and compose comprehensive papers.",
    max_loops=1,
    agents=[
        researcher_agent,
        scraper_agent,
        parser_agent,
        composer_agent,
    ],
    output_type="all",
)

def execute_swarm_task(task_description: str):
    """Execute a multi-agent swarm task."""
    logger.info(f"Starting swarm task: {task_description}")
    try:
        result = swarm_router.run(task_description)
        logger.success("Swarm task completed successfully.")
        print("Final Comprehensive Paper:\n")
        print(result)
    except Exception as e:
        logger.error(f"Error during swarm execution: {e}")
        print(f"An error occurred: {e}")

# Interactive command-line interface
def interactive_chat():
    print("Welcome to the Multi-Agent Swarm Research Interface. Type 'exit' or 'quit' to exit.")
    while True:
        user_input = input("Enter your research topic or query: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif not user_input:
            print("Input cannot be empty. Please enter a valid research topic or query.")
            continue
        try:
            execute_swarm_task(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    interactive_chat()
