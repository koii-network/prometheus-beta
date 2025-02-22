def log_with_indent(message, indent_level=0, indent_char=' ', log_func=print):
    """
    Log a message with specified indentation.
    
    Args:
        message (str): The message to log
        indent_level (int, optional): Number of indentation levels. Defaults to 0.
        indent_char (str, optional): Character used for indentation. Defaults to space.
        log_func (callable, optional): Logging function to use. Defaults to print.
    
    Returns:
        str: The indented message
    """
    # Validate inputs
    if not isinstance(indent_level, int):
        raise ValueError("Indent level must be an integer")
    
    if len(indent_char) != 1:
        raise ValueError("Indent character must be a single character")
    
    # Create indentation
    indentation = indent_char * (indent_level * 4)  # 4 spaces per indent level
    
    # Construct and log the indented message
    indented_message = f"{indentation}{message}"
    log_func(indented_message)
    
    return indented_message