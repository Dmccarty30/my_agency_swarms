import os
from swarms import Agent

parser_agent = Agent(
    agent_name="Parser",
    agent_description="Processes and structures the scraped data for analysis.",
    system_prompt="""
    You are a Parser Agent.
    Task: Process the scraped data and structure it into a coherent and analyzable format.
    Ensure that the data is clean and well-organized.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="parser_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)
