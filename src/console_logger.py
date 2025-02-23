def log_message(message: str) -> None:
    """
    Log a simple message to the console.

    Args:
        message (str): The message to be logged.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the message is empty.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not message.strip():
        raise ValueError("Message cannot be empty")
    
    # Log the message to console
    print(message)