"""
Multi-line message logging utility.

This module provides functionality to log multi-line messages 
with optional separation lines.
"""

def log_multiline_message(message, separator_char='-', separator_length=40):
    """
    Log a multi-line message with optional separator lines.

    Args:
        message (str or list): The message(s) to log. 
            Can be a single string or a list of strings.
        separator_char (str, optional): Character used for separator lines. 
            Defaults to '-'.
        separator_length (int, optional): Length of separator lines. 
            Defaults to 40.

    Returns:
        str: Formatted multi-line log message.

    Raises:
        TypeError: If message is not a string or list of strings.
        ValueError: If separator_char is not a single character.
    """
    # Validate inputs
    if not isinstance(separator_char, str) or len(separator_char) != 1:
        raise ValueError("Separator must be a single character")

    # Convert single string to list if needed
    if isinstance(message, str):
        message = [message]
    
    # Validate message is a list of strings
    if not isinstance(message, list) or not all(isinstance(m, str) for m in message):
        raise TypeError("Message must be a string or list of strings")

    # Create separator line
    separator = separator_char * separator_length

    # Build log message
    log_lines = []
    
    # Add top separator
    log_lines.append(separator)
    
    # Add message lines
    for line in message:
        log_lines.append(line)
    
    # Add bottom separator
    log_lines.append(separator)

    # Join lines and return
    return '\n'.join(log_lines)