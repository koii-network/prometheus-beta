from typing import Literal

def log_with_font_size(message: str, size: Literal['small', 'medium', 'large', 'xlarge'] = 'medium') -> str:
    """
    Log output with different font sizes using HTML-like formatting.
    
    Args:
        message (str): The message to be logged
        size (str, optional): Font size. Defaults to 'medium'.
                               Options: 'small', 'medium', 'large', 'xlarge'
    
    Returns:
        str: Formatted message with font size
    
    Raises:
        ValueError: If an invalid font size is provided
    """
    font_sizes = {
        'small': '8px',
        'medium': '12px',
        'large': '16px',
        'xlarge': '24px'
    }
    
    if size not in font_sizes:
        raise ValueError(f"Invalid font size. Choose from {list(font_sizes.keys())}")
    
    return f'<span style="font-size: {font_sizes[size]};">{message}</span>'