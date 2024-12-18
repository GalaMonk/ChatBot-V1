# src/tests/test_prompt_manager.py

import unittest
from unittest.mock import patch, mock_open
from src.chatbot.prompt_manager import PromptManager
from src.exceptions.chatbot_exceptions import PromptManagerError
import json

class TestPromptManager(unittest.TestCase):
    def setUp(self):
        self.system_prompts_path = "data/prompts/system_prompts.json"
        self.user_prompts_path = "data/prompts/user_prompts.json"
        self.sample_system_prompts = {
            "default": "Você é um assistente amigável e prestativo.",
            "custom": "Você é um especialista em tecnologia."
        }
        self.sample_user_prompts = {
            "greeting": "Olá! Como posso ajudá-lo hoje?",
            "farewell": "Obrigado por usar nosso serviço. Tenha um ótimo dia!",
            "default": "Desculpe, não entendi. Poderia reformular sua pergunta?"
        }

    @patch("builtins.open", new_callable=mock_open, read_data='{"default": "Você é um assistente amigável e prestativo."}')
    @patch("os.path.exists", return_value=True)
    def test_load_system_prompts_success(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        self.assertEqual(prompt_manager.system_prompts, {"default": "Você é um assistente amigável e prestativo."})
        mock_file.assert_called_with(self.system_prompts_path, 'r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data='{"greeting": "Olá! Como posso ajudá-lo hoje?"}')
    @patch("os.path.exists", return_value=True)
    def test_load_user_prompts_success(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        self.assertEqual(prompt_manager.user_prompts, {"greeting": "Olá! Como posso ajudá-lo hoje?"})
        mock_file.assert_called_with(self.user_prompts_path, 'r', encoding='utf-8')

    @patch("os.path.exists", return_value=False)
    def test_load_system_prompts_file_not_found(self, mock_exists):
        with self.assertRaises(PromptManagerError) as context:
            PromptManager("non_existent_system_prompts.json", self.user_prompts_path)
        self.assertIn("Arquivo de prompts não encontrado", str(context.exception))

    @patch("builtins.open", new_callable=mock_open, read_data='Invalid JSON')
    @patch("os.path.exists", return_value=True)
    def test_load_prompts_json_decode_error(self, mock_exists, mock_file):
        with self.assertRaises(PromptManagerError) as context:
            PromptManager(self.system_prompts_path, self.user_prompts_path)
        self.assertIn("Erro ao decodificar JSON", str(context.exception))

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "default": "Você é um assistente amigável e prestativo.",
        "custom": "Você é um especialista em tecnologia."
    }))
    @patch("os.path.exists", return_value=True)
    def test_get_system_prompt_existing_key(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        prompt = prompt_manager.get_system_prompt("custom")
        self.assertEqual(prompt, "Você é um especialista em tecnologia.")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "default": "Você é um assistente amigável e prestativo."
    }))
    @patch("os.path.exists", return_value=True)
    def test_get_system_prompt_non_existing_key(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        with self.assertRaises(PromptManagerError) as context:
            prompt_manager.get_system_prompt("non_existing_key")
        self.assertIn("Prompt de sistema 'non_existing_key' não encontrado.", str(context.exception))

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "greeting": "Olá! Como posso ajudá-lo hoje?"
    }))
    @patch("os.path.exists", return_value=True)
    def test_get_user_prompt_existing_key(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        prompt = prompt_manager.get_user_prompt("greeting")
        self.assertEqual(prompt, "Olá! Como posso ajudá-lo hoje?")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "greeting": "Olá! Como posso ajudá-lo hoje?"
    }))
    @patch("os.path.exists", return_value=True)
    def test_get_user_prompt_non_existing_key(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        with self.assertRaises(PromptManagerError) as context:
            prompt_manager.get_user_prompt("non_existing_key")
        self.assertIn("Prompt de usuário 'non_existing_key' não encontrado.", str(context.exception))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=True)
    def test_add_system_prompt(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        prompt_manager.add_system_prompt("new_prompt", "Este é um novo prompt de sistema.")
        self.assertIn("new_prompt", prompt_manager.system_prompts)
        self.assertEqual(prompt_manager.system_prompts["new_prompt"], "Este é um novo prompt de sistema.")
        mock_file.assert_called_with(self.system_prompts_path, 'w', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=True)
    def test_add_user_prompt(self, mock_exists, mock_file):
        prompt_manager = PromptManager(self.system_prompts_path, self.user_prompts_path)
        prompt_manager.add_user_prompt("new_user_prompt", "Este é um novo prompt de usuário.")
        self.assertIn("new_user_prompt", prompt_manager.user_prompts)
        self.assertEqual(prompt_manager.user_prompts["new_user_prompt"], "Este é um novo prompt de usuário.")
        mock_file.assert_called_with(self.user_prompts_path, 'w', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
