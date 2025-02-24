"""
Utility module for logging multi-line messages with separation lines.
"""

def log_multiline(message, separator='=', line_length=50):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to be logged.
        separator (str, optional): Character used for separation lines. Defaults to '='.
        line_length (int, optional): Length of separation lines. Defaults to 50.

    Returns:
        str: Formatted multi-line log message.

    Raises:
        TypeError: If message is not a string.
        ValueError: If separator is an empty string or line_length is less than 1.
    """
    # Input validation
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not separator:
        raise ValueError("Separator cannot be an empty string")
    
    if line_length < 1:
        raise ValueError("Line length must be at least 1")

    # Create separation line
    sep_line = separator * line_length

    # Construct the full log message
    return f"{sep_line}\n{message}\n{sep_line}"