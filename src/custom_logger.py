import colorama
from typing import Optional, Literal

# Initialize colorama for cross-platform color support
colorama.init(autoreset=True)

class LogStyle:
    """Predefined log styles for easy logging"""
    RESET = colorama.Fore.RESET
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW
    BLUE = colorama.Fore.BLUE
    MAGENTA = colorama.Fore.MAGENTA
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE

def log_message(
    message: str, 
    color: Optional[str] = None, 
    bold: bool = False, 
    prefix: Optional[str] = None
) -> str:
    """
    Log a message with custom styling and optional color.
    
    Args:
        message (str): The message to log
        color (Optional[str]): Color of the message, from LogStyle colors
        bold (bool, optional): Whether to make the text bold. Defaults to False.
        prefix (Optional[str], optional): Optional prefix for the message
    
    Returns:
        str: Formatted log message
    
    Raises:
        ValueError: If an invalid color is provided
    """
    # Validate color
    valid_colors = [
        LogStyle.RED, LogStyle.GREEN, LogStyle.YELLOW, 
        LogStyle.BLUE, LogStyle.MAGENTA, LogStyle.CYAN, 
        LogStyle.WHITE, None
    ]
    if color not in valid_colors:
        raise ValueError(f"Invalid color. Choose from {valid_colors}")
    
    # Prepare the message
    styled_message = message
    
    # Apply color if specified
    if color:
        styled_message = f"{color}{styled_message}"
    
    # Apply bold if specified
    if bold:
        styled_message = f"\033[1m{styled_message}"
    
    # Add prefix if specified
    if prefix:
        styled_message = f"{prefix} {styled_message}"
    
    # Reset styling at the end
    styled_message += LogStyle.RESET
    
    # Print the message (optional, can be customized)
    print(styled_message)
    
    return styled_message