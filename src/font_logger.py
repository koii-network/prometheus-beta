"""
Module for logging output with different font sizes.

This module provides a flexible logging function that allows 
outputting text with varying font sizes and styles.
"""

class FontSizeError(ValueError):
    """Custom exception for invalid font size inputs."""
    pass

def log_with_font_size(message, size='medium', bold=False, italic=False):
    """
    Log a message with specified font size and optional styling.

    Args:
        message (str): The message to be logged.
        size (str, optional): Font size. 
            Defaults to 'medium'.
            Allowed values: 'small', 'medium', 'large', 'xlarge'
        bold (bool, optional): Whether to make text bold. Defaults to False.
        italic (bool, optional): Whether to make text italic. Defaults to False.

    Returns:
        str: Formatted log message with font size and styling.

    Raises:
        FontSizeError: If an invalid font size is provided.
        TypeError: If message is not a string.
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Validate font size
    valid_sizes = ['small', 'medium', 'large', 'xlarge']
    if size not in valid_sizes:
        raise FontSizeError(f"Invalid font size. Must be one of {valid_sizes}")

    # Apply styling
    styled_message = message
    if bold:
        styled_message = f"**{styled_message}**"
    if italic:
        styled_message = f"*{styled_message}*"

    # Create size-based prefix (simulating font size)
    size_prefixes = {
        'small': '🔹 ',    # Small indicator
        'medium': '🔸 ',   # Medium indicator 
        'large': '🔶 ',    # Large indicator
        'xlarge': '🔷 '    # Extra Large indicator
    }

    # Return formatted log message
    return f"{size_prefixes[size]}{styled_message}"