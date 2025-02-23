import logging

def log_with_emoji(message, level='info', emoji='ð'):
    """
    Log messages with optional emojis and configurable log levels.
    
    Args:
        message (str): The message to log
        level (str, optional): Logging level. Defaults to 'info'.
        emoji (str, optional): Emoji to prepend to the message. Defaults to memo emoji.
    
    Returns:
        None
    
    Raises:
        ValueError: If an invalid log level is provided
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    # Map log levels to logging methods
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning, 
        'error': logging.error,
        'critical': logging.critical
    }
    
    # Validate log level
    level = level.lower()
    if level not in log_levels:
        raise ValueError(f"Invalid log level. Choose from {', '.join(log_levels.keys())}")
    
    # Log message with emoji
    log_method = log_levels[level]
    log_method(f"{emoji} {message}")