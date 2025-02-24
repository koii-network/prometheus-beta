def log_bold(message):
    """
    Log a message in bold text to the console.

    Args:
        message (str): The message to be logged in bold.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the message is empty.

    Returns:
        str: The bolded message that was logged.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not message.strip():
        raise ValueError("Message cannot be empty")
    
    # ANSI escape code for bold text
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    
    # Log the bolded message
    bolded_message = f"{BOLD_START}{message}{BOLD_END}"
    print(bolded_message)
    
    return bolded_message