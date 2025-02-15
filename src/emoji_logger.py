import logging
import emoji

def log_with_emoji(message, level='info', emoji_symbol=None):
    """
    Log a message with an optional emoji symbol.
    
    Args:
        message (str): The message to log
        level (str, optional): Logging level. Defaults to 'info'.
        emoji_symbol (str, optional): Emoji to prepend to the message. 
                                      Can be an emoji name or Unicode emoji.
    
    Returns:
        str: The logged message with emoji (if provided)
    
    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(message)s')
    logger = logging.getLogger(__name__)
    
    # Validate and normalize logging level
    level = level.lower()
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    if level not in log_levels:
        raise ValueError(f"Invalid logging level: {level}. Choose from {list(log_levels.keys())}")
    
    # Add emoji if provided
    if emoji_symbol:
        try:
            # Convert emoji name to Unicode if needed
            emoji_str = emoji.emojize(f":{emoji_symbol}:", language='alias') if not emoji.is_emoji(emoji_symbol) else emoji_symbol
            full_message = f"{emoji_str} {message}"
        except Exception:
            # Fallback to original message if emoji conversion fails
            full_message = message
    else:
        full_message = message
    
    # Log the message
    log_levels[level](full_message)
    
    return full_message