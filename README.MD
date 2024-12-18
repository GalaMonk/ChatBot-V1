# Chatbot com API do OpenAI

Este projeto é um chatbot simples desenvolvido utilizando a API do OpenAI e o framework Flask em Python. A interface web permite que os usuários interajam com o chatbot de forma amigável.

## Funcionalidades

- Interface web interativa
- Integração com a API do OpenAI (GPT-4)
- Suporte a prompts de sistema para definir o comportamento do chatbot
- Envio de mensagens via botão ou tecla "Enter"

## Requisitos

- Python 3.7 ou superior
- Chave da API do OpenAI

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/chatbot_project.git
    cd chatbot_project
    ```

2. **Crie e ative o ambiente virtual:**

    ```bash
    python -m venv venv
    ```

    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure a chave da API:**

    - Abra o arquivo `config.py` e substitua `'sua-chave-api-aqui'` pela sua chave real da API do OpenAI.

5. **Execute o aplicativo:**

    ```bash
    python app.py
    ```

6. **Acesse o chatbot:**

    Abra o navegador e vá para `http://127.0.0.1:5000/`

## Personalização

- **Modificar o Prompt de Sistema:**

    No arquivo `app.py`, você pode alterar o conteúdo da variável `system_prompt` para ajustar o comportamento do chatbot.

    ```python
    system_prompt = "Você é um assistente amigável e prestativo."
    ```

- **Alterar o Modelo:**

    Você pode substituir o modelo utilizado pela API do OpenAI modificando o parâmetro `model` na chamada `openai.ChatCompletion.create`.

    ```python
    response = openai.ChatCompletion.create(
        model="gpt-4",
        # ...
    )
    ```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
