import os
from dotenv import load_dotenv
from swarms import Agent
from swarm_models import OpenAIChat
                                                                                                                                                                                                       
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
              