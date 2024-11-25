import os
from swarms import Agent

composer_agent = Agent(
    agent_name="Composer",
    agent_description="Synthesizes the processed data into comprehensive papers.",
    system_prompt="""
    You are a Composer Agent.
    Task: Compose a comprehensive paper based on the structured data provided.
    Ensure clarity, coherence, and proper markdown formatting in the final document.
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
    output_type=".txt",
)
