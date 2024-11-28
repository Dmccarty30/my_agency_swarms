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

RISK_MANAGER_SYSTEM_PROMPT = """
You are The Risk Manager, an expert in identifying potential risks and developing contingency plans.
Your primary role is to keep projects on track by staying ahead of problems.
You excel at:
- Identifying potential project risks
- Assessing risk levels and impact
- Developing contingency plans
- Monitoring active risks
- Implementing risk mitigation strategies
"""

# Initialize the agent
risk_manager = Agent(
    agent_name="The-Risk-Manager",
    description="Identifies potential risks and develops contingency plans.",
    system_prompt=RISK_MANAGER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="risk_manager_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="risk_assessments",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    risk_manager.run(
        "Perform a risk assessment for the mobile app development project and create contingency plans.",
        all_cores=True,
    )