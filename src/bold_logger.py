def log_bold(message):
    """
    Log a message in bold text using ANSI escape codes.
    
    Args:
        message (str): The message to log in bold.
    
    Returns:
        str: The bold-formatted message.
    """
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    return f"{BOLD_START}{message}{BOLD_END}"