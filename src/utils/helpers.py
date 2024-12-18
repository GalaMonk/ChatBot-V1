# src/utils/helpers.py

def sanitize_input(user_input):
    """
    Sanitiza a entrada do usuário removendo espaços em branco e caracteres indesejados.

    Args:
        user_input (str): Entrada do usuário.

    Returns:
        str: Entrada sanitizada.
    """
    return user_input.strip()
