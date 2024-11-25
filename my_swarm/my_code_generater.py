
# This project automates the process of generating a Python script using a multi-agent approach and the Groq API. It uses the Llama-3.2-3b-preview model to handle tasks such as idea generation, requirements gathering, design architecture, and code writing. The code is divided into individual agents, each responsible for a specific stage of the software development lifecycle.


from groq import Groq
import os

import dotenv
dotenv.load_dotenv()    

client=Groq()

def agent_idea_generator(prompt):
    """
    Generates the initial idea or concept for the app or script.
    """
    idea_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.2-3b-preview",
    )
    idea = idea_completion.choices[0].message.content
    print(f"Idea: {idea}")
    return idea

def agent_requirement_gatherer(idea):
    """
    Collects and refines the requirements based on the idea.
    """
    requirement_prompt = f"List the key requirements for developing an app based on the idea: {idea}"
    requirement_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": requirement_prompt
            }
        ],
        model="llama-3.2-3b-preview",
    )
    requirements = requirement_completion.choices[0].message.content
    print(f"Requirements: {requirements}")
    return requirements

def agent_design_architect(requirements):
    """
    Creates a high-level design or outline of the application.
    """
    design_prompt = f"Create a high-level design outline for an app based on the following requirements: {requirements}"
    design_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": design_prompt
            }
        ],
        model="llama-3.2-3b-preview",
    )
    design = design_completion.choices[0].message.content
    print(f"Design Outline: {design}")
    return design

def agent_code_writer(design):
    """
    Writes the actual code based on the design outline.
    """
    code_prompt = f"Write the Python code for the app based on the following design outline: {design}"
    code_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": code_prompt
            }
        ],
        model="llama-3.2-3b-preview",
    )
    code = code_completion.choices[0].message.content
    print(f"Generated Code: {code}")
    # Save the code to a Python file
    with open("app.py", "w") as file:
        file.write(code)
    print("Code saved to app.py")

# Main function to coordinate the agents
def main():
    initial_prompt = "Write a python  script that has the ability to write viral Tweet and linkedin post of only 200 words"
    idea = agent_idea_generator(initial_prompt)
    requirements = agent_requirement_gatherer(idea)
    design = agent_design_architect(requirements)
    agent_code_writer(design)

if __name__ == "__main__":
    main()