import os
from swarms import Agent

researcher_agent = Agent(
    agent_name="Researcher",
    agent_description="Searches the internet for relevant information on specified topics.",
    system_prompt="""
    You are a Researcher Agent. 
    Task: Search the internet for the most recent and relevant information on the given topic.
    Provide a summary of findings with sources.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="researcher_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)
