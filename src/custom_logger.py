import logging
import colorama
from typing import Optional, Union

def log_with_style(
    message: str, 
    level: str = 'info', 
    color: Optional[str] = None, 
    bold: bool = False, 
    underline: bool = False
) -> None:
    """
    Log a message with custom styling.
    
    Args:
        message (str): The message to log
        level (str, optional): Logging level. Defaults to 'info'.
        color (str, optional): Color of the log message. Defaults to None.
        bold (bool, optional): Make the message bold. Defaults to False.
        underline (bool, optional): Underline the message. Defaults to False.
    
    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Initialize colorama for cross-platform color support
    colorama.init(autoreset=True)
    
    # Define color mapping
    color_map = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'blue': colorama.Fore.BLUE,
        'magenta': colorama.Fore.MAGENTA,
        'cyan': colorama.Fore.CYAN,
        'white': colorama.Fore.WHITE
    }
    
    # Define style modifiers
    style = ''
    if color and color.lower() in color_map:
        style += color_map[color.lower()]
    if bold:
        style += colorama.Style.BRIGHT
    if underline:
        style += '\033[4m'
    
    # Select appropriate logging method based on level
    level = level.lower()
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    
    if level not in log_levels:
        raise ValueError(f"Invalid logging level: {level}")
    
    # Apply styling and log the message
    styled_message = f"{style}{message}{colorama.Style.RESET_ALL}"
    log_levels[level](styled_message)