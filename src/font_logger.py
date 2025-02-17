from typing import Union, Literal

def log_with_font_size(message: str, 
                       font_size: Union[int, Literal['small', 'medium', 'large']] = 'medium') -> str:
    """
    Log a message with specified font size.
    
    Args:
        message (str): The message to log
        font_size (Union[int, Literal['small', 'medium', 'large']], optional): 
            Font size specification. Can be:
            - An integer representing exact pixel size
            - A predefined size: 'small', 'medium', 'large'
            Defaults to 'medium'
    
    Returns:
        str: Formatted log message with font size information
    
    Raises:
        ValueError: If an invalid font size is provided
    """
    # Map predefined sizes to pixel values
    size_map = {
        'small': 10,
        'medium': 14,
        'large': 18
    }
    
    # Validate and convert font size
    if isinstance(font_size, str):
        if font_size.lower() not in size_map:
            raise ValueError(f"Invalid predefined font size. Choose from {list(size_map.keys())}")
        pixel_size = size_map[font_size.lower()]
    elif isinstance(font_size, int):
        if font_size < 1:
            raise ValueError("Font size must be a positive integer")
        pixel_size = font_size
    else:
        raise TypeError("Font size must be a string or integer")
    
    # Create formatted log message
    return f"[Font:{pixel_size}px] {message}"