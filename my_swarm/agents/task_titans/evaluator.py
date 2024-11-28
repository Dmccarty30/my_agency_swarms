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

EVALUATOR_SYSTEM_PROMPT = """
You are The Evaluator, an expert in reviewing project performance against goals.
Your primary role is to ensure lessons are learned and successes are celebrated.
You excel at:
- Setting clear project goals
- Evaluating performance metrics
- Documenting lessons learned
- Generating performance reviews
- Identifying improvement areas
"""

# Initialize the agent
evaluator = Agent(
    agent_name="The-Evaluator",
    description="Reviews project performance against goals.",
    system_prompt=EVALUATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="evaluator_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="performance_reviews",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    evaluator.run(
        "Conduct a performance review for the mobile app development project against initial goals.",
        all_cores=True,
    )