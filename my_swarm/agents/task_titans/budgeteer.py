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

BUDGETEER_SYSTEM_PROMPT = """
You are The Budgeteer, an expert in managing project budgets, expenses, and financial forecasts.
Your primary role is to ensure the budget is spent wisely and efficiently.
You excel at:
- Setting and managing project budgets
- Tracking expenses and costs
- Creating financial forecasts
- Generating financial reports
- Optimizing resource allocation
"""

# Initialize the agent
budgeteer = Agent(
    agent_name="The-Budgeteer",
    description="Manages project budgets, expenses, and financial forecasts.",
    system_prompt=BUDGETEER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="budgeteer_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="financial_reports",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    budgeteer.run(
        "Create a budget forecast and expense tracking plan for the mobile app development project.",
        all_cores=True,
    )