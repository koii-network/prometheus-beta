import logging

def emoji_log(message, level='info', emoji=None):
    """
    Log messages with optional emojis for different log levels.
    
    :param message: The log message to be logged
    :param level: Logging level (default: 'info')
    :param emoji: Optional custom emoji. If None, uses predefined emojis for log levels
    """
    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Predefined emojis for different log levels
    default_emojis = {
        'debug': '🔍',
        'info': '📝',
        'warning': '⚠️',
        'error': '❌',
        'critical': '🚨'
    }
    
    # Validate log level
    level = level.lower()
    if level not in ['debug', 'info', 'warning', 'error', 'critical']:
        raise ValueError(f"Invalid log level: {level}")
    
    # Choose emoji
    selected_emoji = emoji or default_emojis.get(level, '')
    
    # Combine emoji with message
    full_message = f"{selected_emoji} {message}"
    
    # Log based on level
    log_method = getattr(logging, level)
    log_method(full_message)