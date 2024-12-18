# src/tests/test_api_client.py

import unittest
from unittest.mock import patch, MagicMock
from src.chatbot.api_client import OpenAIClient
from src.exceptions.chatbot_exceptions import APIClientError

class TestOpenAIClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.client = OpenAIClient(api_key=self.api_key)
        self.messages = [
            {"role": "system", "content": "Você é um assistente amigável."},
            {"role": "user", "content": "Olá, como você está?"}
        ]

    @patch('openai.ChatCompletion.create')
    def test_get_response_success(self, mock_create):
        # Configurar o mock para retornar uma resposta simulada
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message={"content": "Estou bem, obrigado! Como posso ajudar você hoje?"})
        ]
        mock_create.return_value = mock_response

        response = self.client.get_response(self.messages)
        self.assertEqual(response, "Estou bem, obrigado! Como posso ajudar você hoje?")
        mock_create.assert_called_once_with(
            model=self.client.model,
            messages=self.messages,
            max_tokens=self.client.max_tokens,
            temperature=self.client.temperature,
        )

    @patch('openai.ChatCompletion.create')
    def test_get_response_failure(self, mock_create):
        # Configurar o mock para levantar uma exceção
        mock_create.side_effect = Exception("Erro na API")

        with self.assertRaises(APIClientError) as context:
            self.client.get_response(self.messages)
        
        self.assertIn("Erro ao chamar a API do OpenAI: Erro na API", str(context.exception))
        mock_create.assert_called_once_with(
            model=self.client.model,
            messages=self.messages,
            max_tokens=self.client.max_tokens,
            temperature=self.client.temperature,
        )

    @patch('openai.ChatCompletion.create')
    def test_get_response_custom_parameters(self, mock_create):
        # Configurar o mock para retornar uma resposta simulada
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message={"content": "Resposta personalizada."})
        ]
        mock_create.return_value = mock_response

        custom_model = "gpt-3.5-turbo"
        custom_max_tokens = 100
        custom_temperature = 0.5

        response = self.client.get_response(
            self.messages,
            model=custom_model,
            max_tokens=custom_max_tokens,
            temperature=custom_temperature
        )

        self.assertEqual(response, "Resposta personalizada.")
        mock_create.assert_called_once_with(
            model=custom_model,
            messages=self.messages,
            max_tokens=custom_max_tokens,
            temperature=custom_temperature,
        )

if __name__ == '__main__':
    unittest.main()
