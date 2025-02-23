"""
Module for logging output with different font sizes.

This module provides a flexible logging function that allows 
outputting text with varying font sizes and styles.
"""

class FontSizeError(ValueError):
    """Custom exception for invalid font size."""
    pass

def log_with_font_size(message, size=12, style=None):
    """
    Log a message with a specified font size and optional style.

    Args:
        message (str): The message to log.
        size (int, optional): Font size. Defaults to 12.
                              Must be between 6 and 72.
        style (str, optional): Font style. 
                               Can be None, 'bold', 'italic', or 'underline'.

    Returns:
        str: Formatted log message.

    Raises:
        TypeError: If message is not a string.
        FontSizeError: If font size is outside allowed range.
        ValueError: If style is invalid.
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Validate font size
    if not isinstance(size, int):
        raise TypeError("Font size must be an integer")
    
    if size < 6 or size > 72:
        raise FontSizeError("Font size must be between 6 and 72")
    
    # Validate style
    valid_styles = [None, 'bold', 'italic', 'underline']
    if style is not None and style not in valid_styles:
        raise ValueError(f"Invalid style. Must be one of {valid_styles}")
    
    # Format the message based on size and style
    formatted_message = f"[Font Size: {size}] "
    
    if style == 'bold':
        formatted_message += f"**{message}**"
    elif style == 'italic':
        formatted_message += f"*{message}*"
    elif style == 'underline':
        formatted_message += f"_{message}_"
    else:
        formatted_message += message
    
    return formatted_message