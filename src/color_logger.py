import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

def log_colored_message(message, color='white'):
    """
    Log a message in a specified color.
    
    Args:
        message (str): The message to log
        color (str, optional): Color of the message. 
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
    
    Raises:
        ValueError: If an unsupported color is provided
    """
    # Color mapping
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE
    }
    
    # Validate color
    if color.lower() not in color_map:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_map.keys())}")
    
    # Print colored message
    print(f"{color_map[color.lower()]}{message}{Style.RESET_ALL}")