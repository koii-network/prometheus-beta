def log_bold(message):
    """
    Log a message in bold text.
    
    Args:
        message (str): The message to be logged in bold.
    
    Returns:
        str: The message formatted in bold using ANSI escape codes.
    """
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    return f"{BOLD_START}{message}{BOLD_END}"