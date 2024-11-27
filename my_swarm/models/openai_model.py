import os
from swarm_models import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

openai_chat_gpt4o_mini = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="o1-mini",
    temperature=0.1,
)
