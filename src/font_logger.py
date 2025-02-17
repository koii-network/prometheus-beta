from typing import Literal

def log_with_font_size(message: str, size: Literal['small', 'medium', 'large'] = 'medium') -> str:
    """
    Log output with different font sizes.
    
    Args:
        message (str): The message to log
        size (str, optional): Font size. Defaults to 'medium'.
                               Options are 'small', 'medium', 'large'
    
    Returns:
        str: Formatted log message with font size indication
    
    Raises:
        ValueError: If an invalid font size is provided
    """
    # Validate input size
    valid_sizes = ['small', 'medium', 'large']
    if size not in valid_sizes:
        raise ValueError(f"Invalid font size. Must be one of {valid_sizes}")
    
    # Create font size prefixes 
    size_prefixes = {
        'small': '[SMALL] ',
        'medium': '[MEDIUM] ',
        'large': '[LARGE] '
    }
    
    # Return formatted log message
    return f"{size_prefixes[size]}{message}"