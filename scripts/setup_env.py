import subprocess
import sys 
import os

def install_dependences():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def create_directores():
    os.makedirs("data/logs", exist_ok=True)

def create_log_file():
    log_path = "data/logs/chatbot.log"
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("")

def main():
    try:
        print("Instalando dependências...")
        install_dependences()
        print("Criando diretórios necessários...")
        create_directores()
        print("Criando arquivo de log...")
        create_log_file()
        print("Ambiente configurado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro durante a configuração: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

        