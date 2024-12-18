# src/exceptions/chatbot_exceptions.py

class ChatbotError(Exception):
    """Exceção base para erros do chatbot."""
    pass

class APIClientError(ChatbotError):
    """Erro relacionado à comunicação com a API do OpenAI."""
    pass

class PromptManagerError(ChatbotError):
    """Erro relacionado ao gerenciamento de prompts."""
    pass
