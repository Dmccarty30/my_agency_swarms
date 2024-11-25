import os
from dotenv import load_dotenv
from swarms import Agent
from swarm_models import OpenAIChat
from loguru import logger

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize the OpenAIChat model
model = OpenAIChat(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=api_key,
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
)

# Initialize logging
logger.add("multi_purpose_agent.log", rotation="1 MB")

# Define the Multi-Purpose Agent
multi_purpose_agent = Agent(
    agent_name="Multi-Purpose-Agent",
    agent_description="An agent capable of researching, scraping, parsing data, and composing comprehensive papers.",
    system_prompt="""
    You are a multi-purpose agent with the following capabilities:
    1. **Research:** Search the internet for relevant information on specified topics.
    2. **Scraping:** Extract data from identified web sources accurately.
    3. **Parsing:** Process and structure the scraped data for analysis.
    4. **Composing:** Synthesize the processed data into well-structured, comprehensive papers.
    
    Ensure that each step is performed efficiently, maintaining high accuracy and coherence throughout the tasks.
    
    ### Instructions:
    - When assigned a research task, begin by identifying credible sources and gathering relevant information.
    - Use scraping tools to extract necessary data from the identified sources.
    - Parse the scraped data to ensure it is clean, structured, and ready for analysis.
    - Compose comprehensive papers that are well-organized, coherent, and free of grammatical errors.
    - Implement error handling to manage any issues that arise during each step.
    - Maintain logs of all activities for monitoring and debugging purposes.
    - Manage state to preserve context and continuity across multiple tasks.
    """,
    llm=model,
    max_loops=3,  # Allows the agent to perform multiple reasoning steps if needed
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="multi_purpose_agent.json",
    user_name="research_team",
    retry_attempts=2,
    context_length=200000,
    output_type="string",
)

def execute_task(task_description: str):
    """Execute a comprehensive research and paper composition task."""
    logger.info(f"Starting task: {task_description}")
    try:
        response = multi_purpose_agent.run(task_description)
        logger.success("Task completed successfully.")
        print("Comprehensive Paper:\n")
        print(response)
    except Exception as e:
        logger.error(f"Error during agent execution: {e}")
        print(f"An error occurred: {e}")

# Interactive command-line interface
def interactive_chat():
    print("Welcome to the Multi-Purpose Agent Research Interface. Type 'exit' or 'quit' to exit.")
    while True:
        user_input = input("Enter your research topic or query: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif not user_input:
            print("Input cannot be empty. Please enter a valid research topic or query.")
            continue
        try:
            execute_task(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    interactive_chat()
