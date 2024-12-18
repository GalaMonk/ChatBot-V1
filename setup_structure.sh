#!/bin/bash

# setup_structure.sh

# Define o diretório raiz do projeto
PROJECT_ROOT=$(pwd)/chatbot_project

# Cria os diretórios principais
mkdir -p "$PROJECT_ROOT/config"
mkdir -p "$PROJECT_ROOT/src/chatbot"
mkdir -p "$PROJECT_ROOT/src/utils"
mkdir -p "$PROJECT_ROOT/src/exceptions"
mkdir -p "$PROJECT_ROOT/src/tests"
mkdir -p "$PROJECT_ROOT/data/prompts"
mkdir -p "$PROJECT_ROOT/data/logs"
mkdir -p "$PROJECT_ROOT/scripts"
mkdir -p "$PROJECT_ROOT/templates"
mkdir -p "$PROJECT_ROOT/static/css"
mkdir -p "$PROJECT_ROOT/static/js"

# Cria arquivos vazios __init__.py
touch "$PROJECT_ROOT/config/__init__.py"
touch "$PROJECT_ROOT/src/__init__.py"
touch "$PROJECT_ROOT/src/chatbot/__init__.py"
touch "$PROJECT_ROOT/src/utils/__init__.py"
touch "$PROJECT_ROOT/src/exceptions/__init__.py"
touch "$PROJECT_ROOT/src/tests/__init__.py"

# Cria README.md
cat << 'EOF' > "$PROJECT_ROOT/README.md"
# Chatbot com API do OpenAI

Este projeto é um chatbot desenvolvido utilizando a API do OpenAI. A estrutura está organizada de forma modular para facilitar futuras expansões e personalizações.

## Estrutura do Projeto

