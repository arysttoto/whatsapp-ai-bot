from app.ai_prompts import default_prompt
import openai 
from flask import current_app 


class AIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key
    # Add methods for sending prompts and receiving responses
    def reply_to_message(self, message): 
        prompt = default_prompt.format(message_text=message) 
        try:
            response = openai.ChatCompletion.create(
                model=current_app.config["OPENAI_MODEL"],
                messages=[{"role": "user", "content": prompt}],
                temperature=current_app.config["OPENAI_TEMPERATURE"],
                max_tokens=150,
            )
            return response["choices"][0]["message"]["content"].strip()

        except openai.error.OpenAIError:
            return "Sorry, I couldn't process that right now."
