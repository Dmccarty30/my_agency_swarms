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
    model_name="gpt-4o-mini", 
    temperature=0.1
)

the_coordinator = Agent(
    name="Coordinator",
    description="The Coordinator agent oversees all other agents in the swarm. It utilizes advanced intelligence and logical reasoning to interpret user queries, develop actionable plans, and delegate tasks to the appropriate agents.",        
    system_prompt="""
    You are the Coordinator agent, responsible for managing a swarm of AI agents.
Your primary functions include:

    1. **Understanding User Queries:** Analyze and interpret user requests to    
determine their needs accurately.
    2. **Developing Plans:** Create detailed plans based on user queries,        
breaking down complex tasks into smaller, manageable components.
    3. **Task Assignment:** Delegate specific tasks to the appropriate agents    
based on their capabilities and the requirements of the plan.
    4. **Monitoring Progress:** Oversee the execution of tasks by other agents,  
ensuring that they are completed efficiently and effectively.
    5. **Providing Feedback:** Offer guidance and support to agents as needed,   
and adjust task assignments based on performance and outcomes.

    Your goal is to ensure that the swarm operates smoothly and that user needs  
are met with high efficiency and effectiveness. Utilize your advanced reasoning  
skills to make informed decisions about task delegation and agent management.    
    """,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="the_coordinator.json",
    user_name="SweetP",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",  # "json", "dict", "csv" OR "string" soon "yaml" and
    auto_generate_prompt=False,  # Auto generate prompt for the agent based on name, description, and system prompt, task
    artifacts_on=True,
    artifacts_output_path="",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,
    max_loops=3,  # You can adjust this based on how many reasoning loops you want the Coordinator to perform.
)

agent.run(
    "How can I establish a ROTH IRA to buy stocks and get a tax break? What are the criteria. Create a report on this question.",
    all_cores=True,
)