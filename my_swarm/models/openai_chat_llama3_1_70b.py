import os
from swarm_models import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

openai_chat_llama3_1_70b = OpenAIChat(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
)
