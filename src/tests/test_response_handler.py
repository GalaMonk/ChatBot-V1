# src/tests/test_context_manager.py

import unittest
from src.chatbot.context_manager import ContextManager

class TestContextManager(unittest.TestCase):
    def setUp(self):
        self.context_manager = ContextManager()

    def test_add_message(self):
        self.context_manager.add_message("user", "Olá")
        self.context_manager.add_message("assistant", "Olá! Como posso ajudar?")
        self.assertEqual(len(self.context_manager.context), 2)
        self.assertEqual(self.context_manager.context[0], {"role": "user", "content": "Olá"})
        self.assertEqual(self.context_manager.context[1], {"role": "assistant", "content": "Olá! Como posso ajudar?"})

    def test_get_context(self):
        self.context_manager.add_message("user", "Olá")
        self.context_manager.add_message("assistant", "Olá! Como posso ajudar?")
        context = self.context_manager.get_context()
        expected_context = [
            {"role": "user", "content": "Olá"},
            {"role": "assistant", "content": "Olá! Como posso ajudar?"}
        ]
        self.assertEqual(context, expected_context)

    def test_clear_context(self):
        self.context_manager.add_message("user", "Olá")
        self.context_manager.add_message("assistant", "Olá! Como posso ajudar?")
        self.context_manager.clear_context()
        self.assertEqual(len(self.context_manager.context), 0)

    def test_add_multiple_messages(self):
        messages = [
            {"role": "user", "content": "Olá"},
            {"role": "assistant", "content": "Olá! Como posso ajudar?"},
            {"role": "user", "content": "Qual é a previsão do tempo para hoje?"},
            {"role": "assistant", "content": "Hoje está ensolarado com temperaturas em torno de 25°C."}
        ]
        for message in messages:
            self.context_manager.add_message(message["role"], message["content"])
        context = self.context_manager.get_context()
        self.assertEqual(context, messages)

    def test_context_persistence(self):
        self.context_manager.add_message("user", "Olá")
        self.context_manager.add_message("assistant", "Olá! Como posso ajudar?")
        # Simulate restarting the context manager
        new_context_manager = ContextManager()
        self.assertEqual(len(new_context_manager.context), 0)

    def test_add_invalid_role(self):
        with self.assertRaises(ValueError):
            self.context_manager.add_message("invalid_role", "Mensagem inválida")

    def test_add_empty_content(self):
        self.context_manager.add_message("user", "")
        self.assertEqual(len(self.context_manager.context), 1)
        self.assertEqual(self.context_manager.context[0], {"role": "user", "content": ""})

    def test_add_none_content(self):
        with self.assertRaises(TypeError):
            self.context_manager.add_message("user", None)

if __name__ == '__main__':
    unittest.main()
