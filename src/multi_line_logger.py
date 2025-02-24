def log_multiline(message, separator='=', line_length=40):
    """
    Log a multi-line message with top and bottom separators.
    
    Args:
        message (str): The message to log
        separator (str, optional): Character used for separation lines. Defaults to '='.
        line_length (int, optional): Length of separation lines. Defaults to 40.
    
    Returns:
        str: Formatted multi-line log message
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if len(separator) != 1:
        raise ValueError("Separator must be a single character")
    
    if line_length < 1:
        raise ValueError("Line length must be a positive integer")
    
    # Create separation line
    sep_line = separator * line_length
    
    # Construct multi-line log message
    log_lines = [
        sep_line,
        message,
        sep_line
    ]
    
    return '\n'.join(log_lines)