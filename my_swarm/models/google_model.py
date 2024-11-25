import os
from swarm_models import GoogleGemini
from dotenv import load_dotenv

load_dotenv()

google_model = GoogleGemini(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model_name="gemini experimental 1121",
    temperature=0.1,
)
