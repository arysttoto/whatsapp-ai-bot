from app.ai_prompts import default_prompt
import openai 


class AIClient:
    def __init__(self, api_key, model, temperature):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.model = model 
        self.temperature = temperature 


    def generate_reply(self, message): 
        prompt = default_prompt.format(message_text=message) 
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=150,
            )
            return response["choices"][0]["message"]["content"].strip()

        except openai.error.OpenAIError:
            return "Sorry, I couldn't process that right now."
