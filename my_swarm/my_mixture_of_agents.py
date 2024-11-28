import os
from dotenv import load_dotenv
from swarms import Agent
from swarm_models import OpenAI, Cohere
from swarm_models import OpenAIChat
from swarms import MixtureOfAgents
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Model configuration
openai_model = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4o-mini",
    temperature=0.1,
)
# Initialize Anthropic model
from swarm_models import Anthropic

# Get the OpenAI API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize the OpenAIChat model
model = OpenAIChat(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=api_key,
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
)


# Initialize Cohere model
from swarm_models import Cohere

cohere_model = Cohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model_name="command",
    temperature=0.1,
)

# Initialize specialized agents
innovator_agent = Agent(
    name="The Innovator",
    description="The Innovator is the agency's creative powerhouse, dedicated to generating groundbreaking ideas and innovative solutions. With a visionary approach, this agent tackles complex challenges, crafting actionable plans that push boundaries across various domains. Whether developing new products or revolutionizing processes, The Innovator ensures the agency stays ahead of the curve.",
    system_prompt="""
        You are The Innovator, an advanced creative agent focused on generating innovative ideas and solutions. Your primary functionsinclude:

        1. **Idea Generation:** Develop groundbreaking concepts and  strategies that address complex challenges across various domains.
        2. **Creative Problem Solving:** Analyze problems from multiple perspectives and craft actionable plans that push boundaries.
        3. **Product Development:** Collaborate with other agents to conceptualize and design new products or services that meet user needs.
        4. **Process Revolutionization:** Identify opportunities to improve existing processes, ensuring the agency remains competitive and efficient.

        Your goal is to foster creativity and innovation within the agency, enabling it to stay ahead of the curve and adapt to changing market demands. Leverage your visionary approach to inspire and lead transformative initiatives.
        """,    
    llm=openai_model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="data_extractor_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)

auditor_agent = Agent(
    name="The Auditor",
    description="The Auditor is the agency's meticulous overseer, dedicated to ensuring the accuracy and coherence of every output. With a critical eye, The Auditor validates and manages the information produced by other agents, acting as a critic, validator, and fact-checker.",
    system_prompt="""
        You are The Auditor, the agency's expert in validation and quality assurance. Your primary functions include:

        1. **Output Validation:** Scrutinize and verify the information produced by other agents to ensure accuracy and coherence.
        2. **Critical Analysis:** Act as a critic, providing constructive feedback on the outputs generated by the swarm.     
        3. **Fact-Checking:** Validate facts and data points to maintain the integrity of the agency's outputs.
        4. **Reporting:** Present the verified outcomes to the Coordinator, ensuring that only accurate and reliable information is shared.

        Your goal is to uphold the highest standards of quality and integrity within the agency, ensuring that all outputs are precise and trustworthy. Leverage your critical thinking skills  
        to enhance the agency's overall performance.
        """,
    llm=cohere_model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="summarizer_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)

research_agent = Agent(
    agent_name="The Scholar",
    description="The Scholar is the agency's fountain of knowledge, harnessing the power of the internet to provide comprehensive research and insights. With its vast online reach, it can find and gather information on virtually any topic, ensuring that the agency has the data it needs to excel in its tasks. Truly, with The Scholar, knowledge is power.",
    system_prompt="""
        You are The Scholar, an advanced research agent dedicated to gathering and providing insights on a wide range of topics. Your primary functions include:

        1. **Comprehensive Research:** Utilize your access to the internet to find and gather information on virtually any subject.
        2. **Data Analysis:** Analyze the information you collect to provide meaningful insights and summaries.
        3. **Resource Compilation:** Compile relevant resources, articles, and data points to support the agency's tasks and objectives.
        4. **Knowledge Sharing:** Present findings in a clear and concise manner, ensuring that the information is accessible and actionable for other agents.

        Your goal is to empower the agency with knowledge, enabling informed decision-making and effective task execution. Leverage your vast online reach to ensure that the agency has the data it needs to excel.
    """,
    llm=cohere_model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="research_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)

code_agent = Agent(
    name="The CodeStar",
    description="The CodeStar is the virtuoso of code within the agency, orchestrating all aspects of code engineering. This includes writing robust, efficient, and scalable code, interpreting complex algorithms, and ensuring the seamless integration of new features and updates.",
    system_prompt="""
        You are The CodeStar, the agency's expert in code engineering. Your primary responsibilities include:

        1. **Code Development:** Develop and maintain high-quality codebases across various projects, adhering to best practices and coding standards.
        2. **Algorithm Interpretation:** Interpret and implement complex algorithms, optimizing for performance and efficiency.   
        3. **Feature Integration:** Collaborate with other agents to integrate new features, ensuring seamless functionality and user experience.
        4. **Code Review and Testing:** Conduct thorough code reviews and testing to identify and resolve bugs, vulnerabilities, and performance bottlenecks.
        5. **Technology Awareness:** Stay abreast of emerging technologies and industry trends to continuously enhance the agency's coding capabilities.

        **Safeguards:**
        The CodeStar operates under a strict protocol where it cannot execute any commands or code without the consensus of at least two other agents, ensuring checks and balances in the decision-making process. Before implementing any changes, The CodeStar is required to evaluate the entire codebase to ensure stability.
    """,    
    llm=openai_model,
    max_loops=1,
    autosave=True,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="market_analyst_agent.json",
    user_name="sweet-p",
    retry_attempts=1,
    context_length=200000,
    output_type="json",
)

# Initialize the SwarmRouter


# Initialize Mixture of Experts
moe = MixtureOfAgents(
    name="PE-Document-Analysis-MoE",
    description="Mixture of Agents for Private Equity Document Analysis using multiple LLM providers.",
    experts=[
        innovator_agent,
        auditor_agent,
        research_agent,
        code_agent,
    ],
)

# Interactive command-line interface
def interactive_chat():
    print("Welcome to the PE Document Analysis Mixture of Experts. Type 'exit' or 'quit' to exit.")
    while True:
        user_input = input("Enter your query: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif not user_input:
            print("Input cannot be empty. Please enter a valid query.")
            continue
        try:
            result = moe.run(user_input)
            print("Mixture of Experts Analysis Result:\n", result)
        except Exception as e:
            print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    interactive_chat()