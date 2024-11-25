import os
from swarms import Agent

scraper_agent = Agent(
    agent_name="Scraper",
    agent_description="Extracts data from identified web sources accurately.",
    system_prompt="""
    You are a Scraper Agent.
    Task: Extract structured data from the provided web sources.
    Ensure accuracy and completeness in data extraction.
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="scraper_agent.json",
    user_name="research_team",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)
