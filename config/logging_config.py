# config/logging_config.py

import logging

def setup_logging(log_level):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("data/logs/chatbot.log"),
            logging.StreamHandler()
        ]
    )
