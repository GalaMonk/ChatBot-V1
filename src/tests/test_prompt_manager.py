# src/tests/test_response_handler.py

import unittest
from src.chatbot.response_handler import ResponseHandler

class TestResponseHandler(unittest.TestCase):
    def test_format_response_basic(self):
        response = "  Esta é uma resposta.  "
        expected = "Esta é uma resposta."
        formatted = ResponseHandler.format_response(response)
        self.assertEqual(formatted, expected)

    def test_format_response_empty_string(self):
        response = "    "
        expected = ""
        formatted = ResponseHandler.format_response(response)
        self.assertEqual(formatted, expected)

    def test_format_response_no_whitespace(self):
        response = "SemEspaços"
        expected = "SemEspaços"
        formatted = ResponseHandler.format_response(response)
        self.assertEqual(formatted, expected)

    def test_format_response_multiline(self):
        response = "  Linha1\nLinha2  "
        expected = "Linha1\nLinha2"
        formatted = ResponseHandler.format_response(response)
        self.assertEqual(formatted, expected)

    def test_format_response_none(self):
        response = None
        with self.assertRaises(AttributeError):
            ResponseHandler.format_response(response)

if __name__ == '__main__':
    unittest.main()
