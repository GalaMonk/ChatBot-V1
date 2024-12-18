import openai
from config.config import Config
from src.exceptions.chatbot_exceptions import APIClientError

class OpenAIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or Config.OPEN_API_KEY
        openai.api_key = self.api_key

    def get_response(self, messages, model=Config.MODEL_NAME, max_tokens=Config.MAX_TOKENS, temperature=Config.TEMPERATURE):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            raise APIClientError(f"Erro ao chamar a API do OpenAI: {e}")
