def log_multiline(message, separator='=', line_length=50):
    """
    Log a multi-line message with optional separation lines.
    
    Args:
        message (str, list, or any): The message(s) to log
        separator (str, optional): Character used for separation lines. Defaults to '='.
        line_length (int, optional): Length of separation lines. Defaults to 50.
    
    Returns:
        str: Formatted multi-line log message
    """
    # Convert single string or non-iterable to list
    if isinstance(message, str):
        message = [message]
    elif not isinstance(message, list):
        message = [message]
    
    # Validate inputs
    if not isinstance(separator, str) or len(separator) != 1:
        raise ValueError("Separator must be a single character")
    
    if not isinstance(line_length, int) or line_length < 1:
        raise ValueError("Line length must be a positive integer")
    
    # Create separation line
    sep_line = separator * line_length
    
    # Build log message
    log_lines = [sep_line]
    for msg in message:
        log_lines.append(str(msg))
        log_lines.append(sep_line)
    
    return '\n'.join(log_lines)