import logging
import emoji

def log_with_emoji(message, level='info', emoji_symbol=None):
    """
    Log a message with an optional emoji symbol.
    
    Args:
        message (str): The message to log
        level (str, optional): Logging level. Defaults to 'info'.
        emoji_symbol (str, optional): Emoji to prepend to the message. 
                                      If None, a default emoji is chosen based on log level.
    
    Returns:
        str: The logged message with emoji
    
    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(message)s')
    logger = logging.getLogger(__name__)
    
    # Default emoji mapping
    default_emojis = {
        'debug': '🔍',    # magnifying glass
        'info': 'ℹ️',     # information
        'warning': '⚠️',  # warning sign
        'error': '❌',    # cross mark
        'critical': '🚨'  # rotating light
    }
    
    # Validate and normalize log level
    level = level.lower()
    if level not in default_emojis:
        raise ValueError(f"Invalid log level. Choose from {list(default_emojis.keys())}")
    
    # Choose emoji
    if emoji_symbol is None:
        emoji_symbol = default_emojis[level]
    
    # Ensure emoji is valid
    try:
        emoji_symbol = emoji.emojize(emoji_symbol, language='alias')
    except TypeError:
        # If emoji is already a valid emoji, use as-is
        pass
    
    # Construct full message with emoji
    full_message = f"{emoji_symbol} {message}"
    
    # Log based on level
    if level == 'debug':
        logger.debug(full_message)
    elif level == 'info':
        logger.info(full_message)
    elif level == 'warning':
        logger.warning(full_message)
    elif level == 'error':
        logger.error(full_message)
    elif level == 'critical':
        logger.critical(full_message)
    
    return full_message