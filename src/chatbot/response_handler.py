# src/chatbot/response_handler.py

class ResponseHandler:
    @staticmethod
    def format_response(response):
        """
        Formata a resposta recebida da API do OpenAI.
        
        Args:
            response (str): Resposta bruta da API.
        
        Returns:
            str: Resposta formatada.
        """
        # Implementar formatação específica, se necessário
        return response.strip()
