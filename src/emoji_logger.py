import emoji

def log_with_emoji(message, emoji_symbol=None, log_level='info'):
    """
    Log a message with an optional emoji symbol.

    Args:
        message (str): The message to log
        emoji_symbol (str, optional): An emoji or symbol to prepend to the message
        log_level (str, optional): Logging level. Defaults to 'info'.
            Supports 'debug', 'info', 'warning', 'error', 'critical'

    Returns:
        None

    Raises:
        ValueError: If an invalid log level is provided
        TypeError: If message is not a string
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Prepare the log message
    if emoji_symbol:
        # Ensure the emoji is valid
        try:
            processed_emoji = emoji.emojize(emoji_symbol, language='alias') if ':' in emoji_symbol else emoji_symbol
            full_message = f"{processed_emoji} {message}"
        except Exception:
            full_message = message
    else:
        full_message = message

    # Log based on level
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']

    # Validate log level
    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level: {log_level}. Must be one of {log_levels}")

    # Print the message (default to print without decoration for simplicity)
    print(full_message)