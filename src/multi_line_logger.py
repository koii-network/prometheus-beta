"""
Module for multi-line logging with separation lines.

This module provides a utility function for logging multi-line messages
with customizable separation lines.
"""

def log_multiline(message, separator='=', line_length=40, logger=None):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to be logged.
        separator (str, optional): Character used for separation lines. Defaults to '='.
        line_length (int, optional): Length of separation lines. Defaults to 40.
        logger (callable, optional): Logging function to use. Defaults to print.

    Raises:
        ValueError: If separator is an empty string or message is not a string.
        TypeError: If line_length is not a positive integer.
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not separator:
        raise ValueError("Separator cannot be an empty string")
    
    if not isinstance(line_length, int) or line_length <= 0:
        raise TypeError("Line length must be a positive integer")
    
    # Use print as default logger if no logger is provided
    log_func = logger or print
    
    # Create separation line
    sep_line = separator * line_length
    
    # Log the message with separation lines
    log_func(sep_line)
    log_func(message)
    log_func(sep_line)