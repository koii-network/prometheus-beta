import logging

def log_multiline(message, level=logging.INFO, separator='*', separator_length=40):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to be logged
        level (int, optional): Logging level. Defaults to logging.INFO.
        separator (str, optional): Character used for separation lines. Defaults to '*'.
        separator_length (int, optional): Length of separation lines. Defaults to 40.

    Raises:
        TypeError: If message is not a string or separator is not a string
        ValueError: If separator is empty or separator_length is less than 1
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string")
    
    if not separator:
        raise ValueError("Separator cannot be an empty string")
    
    if separator_length < 1:
        raise ValueError("Separator length must be at least 1")

    # Create the logger
    logger = logging.getLogger(__name__)

    # Create separation line
    sep_line = separator * separator_length

    # Log the message with separation lines
    logger.log(level, sep_line)
    logger.log(level, message)
    logger.log(level, sep_line)

    return sep_line  # Return the separator line for potential additional use