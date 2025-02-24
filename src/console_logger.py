def log_message(message):
    """
    Log a simple message to the console.

    Args:
        message (str): The message to be logged to the console.

    Raises:
        TypeError: If the message is not a string.
        ValueError: If the message is an empty string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not message.strip():
        raise ValueError("Message cannot be empty")
    
    # Log the message to the console
    print(message)