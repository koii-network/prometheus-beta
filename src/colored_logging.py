from colorama import init, Fore, Style

def log_colored_message(message, color='GREEN'):
    """
    Log a message in a specified color.
    
    Args:
        message (str): The message to log
        color (str, optional): Color of the message. 
                               Supports: 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN'. 
                               Defaults to 'GREEN'.
    
    Raises:
        ValueError: If an unsupported color is provided
    """
    # Initialize colorama for cross-platform color support
    init()
    
    # Map color input to colorama colors
    color_map = {
        'RED': Fore.RED,
        'GREEN': Fore.GREEN,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN
    }
    
    # Validate color input
    color = color.upper()
    if color not in color_map:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_map.keys())}")
    
    # Print the colored message
    print(f"{color_map[color]}{message}{Style.RESET_ALL}")