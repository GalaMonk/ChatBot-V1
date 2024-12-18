# src/chatbot/prompt_manager.py

import json
import os
from config.config import Config
from src.exceptions.chatbot_exceptions import PromptManagerError

class PromptManager:
    def __init__(self, system_prompts_path=None, user_prompts_path=None):
        # Obtém o diretório atual do arquivo prompt_manager.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define os caminhos absolutos para os arquivos de prompts
        self.system_prompts_path = system_prompts_path or os.path.join(current_dir, "../../data/prompts/system_prompts.json")
        self.user_prompts_path = user_prompts_path or os.path.join(current_dir, "../../data/prompts/user_prompts.json")
        
        self.system_prompts = self.load_prompts(self.system_prompts_path)
        self.user_prompts = self.load_prompts(self.user_prompts_path)

    def load_prompts(self, path):
        if not os.path.exists(path):
            raise PromptManagerError(f"Arquivo de prompts não encontrado: {path}")
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise PromptManagerError(f"Erro ao decodificar JSON em {path}: {e}")

    def get_system_prompt(self, key="default"):
        prompt = self.system_prompts.get(key)
        if not prompt:
            raise PromptManagerError(f"Prompt de sistema '{key}' não encontrado.")
        return prompt

    def get_user_prompt(self, key="default"):
        prompt = self.user_prompts.get(key)
        if not prompt:
            raise PromptManagerError(f"Prompt de usuário '{key}' não encontrado.")
        return prompt

    def add_system_prompt(self, key, prompt):
        self.system_prompts[key] = prompt
        self.save_prompts(self.system_prompts_path, self.system_prompts)

    def add_user_prompt(self, key, prompt):
        self.user_prompts[key] = prompt
        self.save_prompts(self.user_prompts_path, self.user_prompts)

    def save_prompts(self, path, prompts):
        try:
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(prompts, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise PromptManagerError(f"Erro ao salvar prompts em {path}: {e}")
