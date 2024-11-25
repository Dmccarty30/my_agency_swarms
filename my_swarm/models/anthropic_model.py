import os
from swarm_models import Anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_model = Anthropic(
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    model_name="claude-sonnet-2024-10-22",
    temperature=0.1,
)
