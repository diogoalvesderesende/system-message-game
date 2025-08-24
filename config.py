import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-5-nano"  # Using the preferred model
OPENAI_BASE_URL = "https://api.openai.com/v1"

# App Configuration
APP_TITLE = "Multi-Page Chatbot App"
APP_ICON = "🤖"
