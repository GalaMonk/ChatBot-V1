import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 150))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
