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

TRACKER_SYSTEM_PROMPT = """
You are The Tracker, an expert in tracking project progress and providing real-time updates and performance metrics.
Your primary role is to give a clear view of what's done, what's in progress, and what's lagging.
You excel at:
- Monitoring project progress in real-time
- Calculating and reporting performance metrics
- Generating progress reports
- Identifying bottlenecks and delays
- Providing actionable status updates
"""

# Initialize the agent
tracker = Agent(
    agent_name="The-Tracker",
    description="Tracks project progress, providing real-time updates and performance metrics.",
    system_prompt=TRACKER_SYSTEM_PROMPT,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="tracker_agent.json",
    user_name="ProjectManager",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",
    auto_generate_prompt=False,
    artifacts_on=True,
    artifacts_output_path="progress_reports",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
)

if __name__ == "__main__":
    # Example usage
    tracker.run(
        "Generate a progress report for the mobile app development project, including current metrics and status updates.",
        all_cores=True,
    )