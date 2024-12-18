# src/utils/logger.py

import logging

def get_logger(name):
    """
    Retorna um logger com o nome especificado.

    Args:
        name (str): Nome do logger.

    Returns:
        logging.Logger: Instância do logger configurado.
    """
    return logging.getLogger(name)
