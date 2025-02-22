def log_multi_line(message, separator='=', width=80):
    """
    Log a multi-line message with separation lines.
    
    Args:
        message (str): The multi-line message to log
        separator (str, optional): Character used for separation lines. Defaults to '='.
        width (int, optional): Width of the separation lines. Defaults to 80.
    
    Returns:
        str: Formatted multi-line log message
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if len(separator) != 1:
        raise ValueError("Separator must be a single character")
    
    # Split message into lines
    lines = message.split('\n')
    
    # Create separation line
    sep_line = separator * width
    
    # Construct formatted log message
    log_lines = [sep_line]
    log_lines.extend(lines)
    log_lines.append(sep_line)
    
    return '\n'.join(log_lines)