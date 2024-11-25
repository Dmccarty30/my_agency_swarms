import os
from swarm_models import Cohere
from dotenv import load_dotenv

load_dotenv()

cohere_model = Cohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model_name="command r-plus",
    temperature=0.1,
)
