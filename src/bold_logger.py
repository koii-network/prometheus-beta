def log_bold(message):
    """
    Log a message in bold text using ANSI escape codes.
    
    Args:
        message (str): The message to log in bold.
    """
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    print(f"{BOLD_START}{message}{BOLD_END}")