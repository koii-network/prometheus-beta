import colorama
from typing import Literal, Optional

# Initialize colorama for cross-platform color support
colorama.init(autoreset=True)

def log_message(
    message: str, 
    level: Literal['info', 'warning', 'error', 'success'] = 'info', 
    prefix: Optional[str] = None
) -> str:
    """
    Log a message with custom styling based on the log level.
    
    Args:
        message (str): The message to log
        level (str, optional): Log level determining color and style. Defaults to 'info'.
        prefix (str, optional): Custom prefix to add before the message. Defaults to None.
    
    Returns:
        str: The formatted log message
    
    Raises:
        ValueError: If an invalid log level is provided
    """
    # Define color and prefix mappings
    color_map = {
        'info': colorama.Fore.BLUE,
        'warning': colorama.Fore.YELLOW,
        'error': colorama.Fore.RED,
        'success': colorama.Fore.GREEN
    }
    
    # Validate log level
    if level not in color_map:
        raise ValueError(f"Invalid log level: {level}. Must be one of {list(color_map.keys())}")
    
    # Determine color
    color = color_map[level]
    
    # Create prefix if not provided
    if prefix is None:
        prefix = f"[{level.upper()}] "
    
    # Format the log message
    formatted_message = f"{color}{prefix}{message}{colorama.Fore.RESET}"
    
    # Print the message (for actual logging)
    print(formatted_message)
    
    return formatted_message