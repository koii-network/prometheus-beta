import colorama
from typing import Optional, Literal

class LogStyle:
    """
    Defines color and formatting options for log messages.
    """
    RESET = colorama.Fore.RESET
    
    # Color options
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW
    BLUE = colorama.Fore.BLUE
    MAGENTA = colorama.Fore.MAGENTA
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE

    # Style options
    BRIGHT = colorama.Style.BRIGHT
    DIM = colorama.Style.DIM
    NORMAL = colorama.Style.NORMAL

def log_message(
    message: str, 
    color: Optional[str] = None, 
    style: Optional[str] = None, 
    prefix: Optional[str] = None
) -> str:
    """
    Log a message with custom styling and optional prefix.

    Args:
        message (str): The message to log
        color (Optional[str]): Color of the message. 
            Options: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
        style (Optional[str]): Text style. 
            Options: 'bright', 'dim', 'normal'
        prefix (Optional[str]): Optional prefix for the message

    Returns:
        str: Formatted log message

    Raises:
        ValueError: If an invalid color or style is provided
    """
    # Initialize colorama
    colorama.init(autoreset=True)

    # Validate and map color
    color_map = {
        'red': LogStyle.RED,
        'green': LogStyle.GREEN,
        'yellow': LogStyle.YELLOW,
        'blue': LogStyle.BLUE,
        'magenta': LogStyle.MAGENTA,
        'cyan': LogStyle.CYAN,
        'white': LogStyle.WHITE
    }
    if color and color.lower() not in color_map:
        raise ValueError(f"Invalid color: {color}. Choose from {list(color_map.keys())}")

    # Validate and map style
    style_map = {
        'bright': LogStyle.BRIGHT,
        'dim': LogStyle.DIM,
        'normal': LogStyle.NORMAL
    }
    if style and style.lower() not in style_map:
        raise ValueError(f"Invalid style: {style}. Choose from {list(style_map.keys())}")

    # Apply color and style
    color_code = color_map.get(color.lower(), '') if color else ''
    style_code = style_map.get(style.lower(), '') if style else ''

    # Construct message
    full_message = f"{prefix + ' ' if prefix else ''}{message}"
    styled_message = f"{style_code}{color_code}{full_message}{LogStyle.RESET}"

    # Print the message (optional, depending on requirements)
    print(styled_message)

    return styled_message