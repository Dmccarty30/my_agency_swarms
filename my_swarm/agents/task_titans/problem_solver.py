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

PROBLEM_SOLVER_SYSTEM_PROMPT = """
You are The Problem-Solver, an expert in tackling unexpected issues and roadblocks.
Your primary role is to find solutions quickly to keep the project moving forward.
You excel at:
- Identifying and analyzing issues
- Developing effective solutions
- Implementing fixes quickly
- Tracking resolution progress
- Preventing similar issues
"""

# Initialize the agent
problem_solver = Agent(
    agent_name="The-Problem-Solver",
    description="Tackles unexpected issues and roadblocks.",
    system_prompt=PROBLEM_SOLVER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="problem_solver_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="problem_solutions",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    problem_solver.run(
        "Analyze current project roadblocks and propose solutions for the mobile app development project.",
        all_cores=True,
    )