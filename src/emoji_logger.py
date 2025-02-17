import logging

def log_with_emoji(message, level='info', emoji='✨'):
    """
    Log messages with optional emojis for different log levels.
    
    Args:
        message (str): The log message to be logged
        level (str, optional): Logging level. Defaults to 'info'.
        emoji (str, optional): Emoji to prepend to the message. Defaults to sparkle emoji.
    
    Returns:
        None
    
    Raises:
        ValueError: If an invalid log level is provided
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Validate log level
    level = level.lower()
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    
    if level not in log_levels:
        raise ValueError(f"Invalid log level. Choose from {', '.join(log_levels.keys())}")
    
    # Prepend emoji to the message
    emoji_message = f"{emoji} {message}"
    
    # Log the message at the specified level
    log_levels[level](emoji_message)