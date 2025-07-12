"""
Configuration Management

This module provides configuration management for the WhatsApp AI bot.
It loads environment variables and provides default values for all
required API credentials and settings.

The configuration system supports:
- Environment variable loading with dotenv
- Default values for development
- Centralized configuration management
- WhatsApp Business API settings
- OpenAI API settings

Environment Variables:
    WHATSAPP_API_URL: Base URL for WhatsApp Business API
    WHATSAPP_WEBHOOK_VERIFY_TOKEN: Token for webhook verification
    WHATSAPP_ACCESS_TOKEN: Access token for WhatsApp API
    WHATSAPP_PHONE_NUMBER_ID: WhatsApp phone number ID
    OPENAI_API_KEY: OpenAI API key for AI responses
    OPENAI_MODEL: OpenAI model to use (e.g., gpt-3.5-turbo)
    OPENAI_TEMPERATURE: Temperature for AI response creativity

Example:
    Create a .env file with your API credentials:
    WHATSAPP_API_URL=https://graph.facebook.com/v23.0
    WHATSAPP_WEBHOOK_VERIFY_TOKEN=your_verify_token
    WHATSAPP_ACCESS_TOKEN=your_access_token
    WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_MODEL=gpt-3.5-turbo
    OPENAI_TEMPERATURE=0.7
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    Configuration class for WhatsApp AI bot settings.

    This class centralizes all configuration variables needed for the
    WhatsApp AI bot, including API credentials, model settings, and
    webhook configuration. It loads values from environment variables
    with sensible defaults for development.

    All configuration values are loaded from environment variables
    when the class is imported. Make sure to set up your .env file
    with the required API credentials before running the application.
    """

    # WhatsApp Business API Configuration
    WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "your-whatsapp-api-url")
    WHATSAPP_WEBHOOK_VERIFY_TOKEN = os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token")
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "your-whatsapp-access-token") 
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "your-whatsapp-phone-number-id")

    # OpenAI API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "your-openai-model")
    OPENAI_TEMPERATURE = os.getenv("OPENAI_TEMPERATURE", 'your-openai-temperature') 
    # Add more configuration variables as needed
