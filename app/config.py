import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "your-whatsapp-api-url")
    WHATSAPP_WEBHOOK_VERIFY_TOKEN = os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token")
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "your-whatsapp-access-token") 
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "your-whatsapp-phone-number-id")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "your-openai-model")
    OPENAI_TEMPERATURE = os.getenv("OPENAI_TEMPERATURE", 'your-openai-temperature') 
    # Add more configuration variables as needed
