from dotenv import load_dotenv
from pathlib import Path
import os

# Get absolute path of .env
env_path = Path(__file__).resolve().parent / ".env"

# Load it explicitly
load_dotenv(dotenv_path=env_path)

# Fetch key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("ENV PATH:", env_path)
print("FILE EXISTS:", env_path.exists())
print("API KEY:", GROQ_API_KEY)