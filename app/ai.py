"""
OpenAI Integration Client

This module provides a client for interacting with OpenAI's GPT models to generate
automated responses for WhatsApp messages. It handles API communication, prompt
formatting, and error handling for AI-generated responses.

The client supports:
- Text generation using OpenAI's ChatCompletion API
- Customizable prompts and model parameters
- Error handling for API failures
- Temperature and token limit configuration

Example:
    client = AIClient(
        api_key="your_openai_api_key",
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    response = client.generate_reply("Hello, how can you help me?")
"""

from app.ai_prompts import default_prompt
import openai 
from openai import OpenAIError
from app.errors import RetryableError


class AIClient:
    """
    Client for interacting with OpenAI's GPT models.

    This class handles all communication with OpenAI's API for generating
    automated responses to WhatsApp messages. It manages API configuration,
    prompt formatting, and error handling.

    Attributes:
        api_key (str): OpenAI API key for authentication
        model (str): OpenAI model to use for text generation
        temperature (float): Temperature parameter for response creativity
    """

    def __init__(self, api_key, model, temperature):
        """
        Initialize AI client with OpenAI configuration.

        Args:
            api_key (str): OpenAI API key for authentication
            model (str): OpenAI model name (e.g., "gpt-3.5-turbo", "gpt-4")
            temperature (float): Temperature parameter (0.0-2.0) controlling
                               response randomness. Higher values = more creative
        """
        self.api_key = api_key
        openai.api_key = self.api_key
        self.model = model 
        self.temperature = temperature 

    def generate_reply(self, message):
        """
        Generate AI-powered reply to a WhatsApp message.

        Uses OpenAI's ChatCompletion API to generate a contextual response
        to incoming WhatsApp messages. The response is formatted using a
        predefined prompt template.

        Args:
            message (str): The incoming WhatsApp message to respond to

        Returns:
            str: AI-generated response message

        Raises:
            RetryableError: If OpenAI API call fails or returns an error

        Note:
            Uses a default prompt template that can be customized in ai_prompts.py.
            Response is limited to 150 tokens for WhatsApp message length constraints.
        """
        prompt = default_prompt.format(message_text=message) 
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=150,
            )
            return response["choices"][0]["message"]["content"].strip()

        except OpenAIError as error:
            raise RetryableError(f"Error during AI response generation: {error}")
