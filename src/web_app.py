import sys
import os

# Adicionar o diretório raiz do projeto ao sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from flask import Flask, request, jsonify, render_template
from config.config import Config
from config.logging_config import setup_logging
from src.chatbot.api_client import OpenAIClient
from src.chatbot.prompt_manager import PromptManager
from src.chatbot.context_manager import ContextManager
from src.chatbot.response_handler import ResponseHandler
from src.utils.logger import get_logger
from src.utils.helpers import sanitize_input

app = Flask(__name__)

# Configurar logging
setup_logging(Config.LOG_LEVEL)
logger = get_logger(__name__)
logger.info("Iniciando a aplicação web do Chatbot")

# Inicializar componentes
client = OpenAIClient(api_key=Config.OPENAI_API_KEY)
prompt_manager = PromptManager()
context_manager = ContextManager()
response_handler = ResponseHandler()

# Obter prompt de sistema e adicionar ao contexto
system_prompt = prompt_manager.get_system_prompt()
context_manager.add_message("system", system_prompt)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = sanitize_input(data.get("message", ""))

        if user_message.lower() in ["sair", "exit", "quit"]:
            return jsonify({"response": "Até logo!"})

        # Adicionar mensagem do usuário ao contexto
        context_manager.add_message("user", user_message)

        # Obter contexto atual
        messages = context_manager.get_context()

        # Obter resposta da API do OpenAI
        raw_response = client.get_response(messages)

        # Formatar resposta
        formatted_response = response_handler.format_response(raw_response)

        # Adicionar mensagem do assistente ao contexto
        context_manager.add_message("assistant", formatted_response)

        return jsonify({"response": formatted_response})

    except Exception as e:
        logger.error(f"Erro no endpoint /chat: {e}")
        return jsonify({"response": "Desculpe, ocorreu um erro ao processar sua solicitação."}), 500

if __name__ == "__main__":
    app.run(debug=True)
