import os


class Config:
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "your-whatsapp-token")
    AI_API_KEY = os.getenv("AI_API_KEY", "your-ai-api-key")
    # Add more configuration variables as needed
