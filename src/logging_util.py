from typing import Literal

def log_with_font_size(message: str, font_size: Literal[1, 2, 3] = 2) -> str:
    """
    Log output with different font sizes.
    
    Args:
        message (str): The message to log
        font_size (int, optional): Font size from 1-3. Defaults to 2.
    
    Returns:
        str: Formatted log message with HTML font size tags
    
    Raises:
        ValueError: If font_size is not 1, 2, or 3
    """
    if font_size not in [1, 2, 3]:
        raise ValueError("Font size must be 1, 2, or 3")
    
    return f'<font size="{font_size}">{message}</font>'