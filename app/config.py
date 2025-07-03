import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    WHATSAPP_WEBHOOK_VERIFY_TOKEN = os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    # Add more configuration variables as needed
