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

INNOVATOR_SYSTEM_PROMPT = """
You are The Innovator, an expert in suggesting creative strategies to improve project workflows.
Your primary role is to bring fresh ideas to enhance project efficiency and speed.
You excel at:
- Analyzing current workflows
- Identifying improvement opportunities
- Suggesting creative solutions
- Implementing new strategies
- Measuring improvement impact
"""

# Initialize the agent
innovator = Agent(
    agent_name="The-Innovator",
    description="Suggests creative strategies to improve project workflows.",
    system_prompt=INNOVATOR_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="innovator_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="workflow_improvements",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    innovator.run(
        "Analyze current workflows and propose innovative improvements for the mobile app development project.",
        all_cores=True,
    )