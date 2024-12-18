# src/main.py

from config.config import Config
from config.logging_config import setup_logging
from src.chatbot.api_client import OpenAIClient
from src.chatbot.prompt_manager import PromptManager
from src.chatbot.context_manager import ContextManager
from src.chatbot.response_handler import ResponseHandler
from src.utils.logger import get_logger
from src.utils.helpers import sanitize_input

def main():
    # Configurar logging
    setup_logging(Config.LOG_LEVEL)
    logger = get_logger(__name__)
    logger.info("Iniciando o Chatbot")
    
    # Verificação temporária
    if not Config.OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY não está configurada.")
        print("Erro: OPENAI_API_KEY não está configurada. Verifique seu arquivo .env.")
        return
    
    # Inicializar componentes
    client = OpenAIClient(api_key=Config.OPENAI_API_KEY)
    prompt_manager = PromptManager()
    context_manager = ContextManager()
    response_handler = ResponseHandler()

    # Obter prompt de sistema
    system_prompt = prompt_manager.get_system_prompt()

    # Adicionar prompt de sistema ao contexto
    context_manager.add_message("system", system_prompt)

    print("Chatbot iniciado. Digite 'sair' para encerrar.")

    while True:
        try:
            user_input = input("Você: ")
            user_input = sanitize_input(user_input)

            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Chatbot: Até logo!")
                break

            # Adicionar mensagem do usuário ao contexto
            context_manager.add_message("user", user_input)

            # Obter contexto atual
            messages = context_manager.get_context()

            # Obter resposta da API do OpenAI
            raw_response = client.get_response(messages)

            # Formatar resposta
            formatted_response = response_handler.format_response(raw_response)

            # Adicionar mensagem do assistente ao contexto
            context_manager.add_message("assistant", formatted_response)

            # Exibir resposta do chatbot
            print(f"Chatbot: {formatted_response}")

        except KeyboardInterrupt:
            print("\nChatbot: Até logo!")
            break
        except Exception as e:
            logger.error(f"Erro no chatbot: {e}")
            print("Chatbot: Desculpe, ocorreu um erro inesperado.")

if __name__ == "__main__":
    main()
