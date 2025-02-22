import logging

def log_with_emoji(message, level='info', emoji=None):
    """
    Log a message with an optional emoji prefix.
    
    :param message: The message to log
    :param level: Logging level (info, warning, error, debug)
    :param emoji: Optional emoji to prepend to the message
    :return: The logged message
    """
    # Configure basic logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    
    # Default emojis for different log levels
    default_emojis = {
        'info': '📝',     # Memo emoji for info
        'warning': '⚠️',  # Warning sign for warnings
        'error': '❌',    # Cross mark for errors
        'debug': '🔍'     # Magnifying glass for debug
    }
    
    # Validate log level
    level = level.lower()
    if level not in ['info', 'warning', 'error', 'debug']:
        raise ValueError(f"Invalid log level: {level}")
    
    # Use provided emoji or default emoji for the log level
    log_emoji = emoji if emoji else default_emojis.get(level, '')
    
    # Prepare the full message with emoji
    full_message = f"{log_emoji} {message}" if log_emoji else message
    
    # Log based on level
    log_method = getattr(logging, level)
    log_method(full_message)
    
    return full_message