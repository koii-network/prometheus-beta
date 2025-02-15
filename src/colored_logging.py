from colorama import init, Fore, Style

def log_colored_message(message, color='GREEN'):
    """
    Log a message in a specified color.
    
    Args:
        message (str): The message to log
        color (str, optional): Color of the message. 
            Supported colors: 'GREEN', 'RED', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN'. 
            Defaults to 'GREEN'.
    
    Returns:
        str: The colored log message
    
    Raises:
        ValueError: If an unsupported color is provided
    """
    # Initialize colorama
    init()
    
    # Map color names to colorama color codes
    color_map = {
        'GREEN': Fore.GREEN,
        'RED': Fore.RED,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN
    }
    
    # Validate color
    color = color.upper()
    if color not in color_map:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_map.keys())}")
    
    # Return colored message
    return f"{color_map[color]}{message}{Style.RESET_ALL}"