import os
from dotenv import load_dotenv
from swarms import Agent
from swarm_models import OpenAIChat
from swarms import MixtureOfExperts

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Model configuration
model = OpenAIChat(
    openai_api_key=api_key,
    model_name="gpt-4o-mini",
    temperature=0.1,
)
# Initialize Anthropic model
from swarm_models import Anthropic

anthropic_model = Anthropic(
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    model_name="claude-sonnet-2024-10-22",
    temperature=0.1,
)
#Initialize Groq model
model = OpenAIChat(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=api_key,
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
)

# Initialize Cohere model
from swarm_models import Cohere

cohere_model = Cohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model_name="command r-plus",
    temperature=0.1,
)

# Initialize Google model
from swarm_models import GoogleGemini

google_model = GoogleGemini(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model_name="gemini experimental 1121",
    temperature=0.1,
)

# Initialize specialized agents
data_extractor_agent = Agent(
    agent_name="Data-Extractor",
    system_prompt="You are a data extraction specialist. Extract relevant information from provided content.",
    llm=OpenAIChat,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="data_extractor_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="all",
)

summarizer_agent = Agent(
    agent_name="Document-Summarizer",
    system_prompt="You are a document summarization specialist. Provide clear and concise summaries.",
    llm=cohere_model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="summarizer_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="all",
)

financial_analyst_agent = Agent(
    agent_name="Financial-Analyst",
    system_prompt="You are a financial analysis specialist. Analyze financial aspects of content.",
    llm=GoogleGemini,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="financial_analyst_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="all",
)

market_analyst_agent = Agent(
    agent_name="Market-Analyst",
    system_prompt="You are a market analysis specialist. Analyze market-related aspects.",
    llm=Anthropic,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="market_analyst_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="all",
)

# Initialize the SwarmRouter


# Initialize Mixture of Experts
moe = MixtureOfExperts(
    name="PE-Document-Analysis-MoE",
    description="Mixture of Experts for Private Equity Document Analysis using multiple LLM providers.",
    experts=[
        data_extractor_agent,
        summarizer_agent,
        financial_analyst_agent,
        market_analyst_agent,
    ],
)

# Interactive command-line interface
def interactive_chat():
    print("Welcome to the PE Document Analysis Mixture of Experts. Type 'exit' or 'quit' to exit.")
    while True:
        user_input = input("Enter your query: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif not user_input:
            print("Input cannot be empty. Please enter a valid query.")
            continue
        try:
            result = moe.run(user_input)
            print("Mixture of Experts Analysis Result:\n", result)
        except Exception as e:
            print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    interactive_chat()
