import colorama
import textwrap
from typing import Optional, Union

colorama.init(autoreset=True)

def log_with_style(
    message: str, 
    style: Optional[str] = None, 
    indent: int = 0, 
    width: int = 80
) -> str:
    """
    Log a message with custom styling and optional formatting.
    
    Args:
        message (str): The message to log
        style (Optional[str]): Color/styling option. 
            Options: 'success', 'warning', 'error', 'info'
        indent (int): Number of spaces to indent the message
        width (int): Maximum width of the wrapped message
    
    Returns:
        str: Formatted and styled log message
    """
    # Define color and style mappings
    styles = {
        'success': colorama.Fore.GREEN,
        'warning': colorama.Fore.YELLOW,
        'error': colorama.Fore.RED,
        'info': colorama.Fore.CYAN,
        None: colorama.Fore.RESET
    }
    
    # Select color based on style, default to reset
    color = styles.get(style, colorama.Fore.RESET)
    
    # Wrap the message with textwrap
    wrapped_message = textwrap.fill(message, width=width)
    
    # Add indentation
    indented_message = '\n'.join(' ' * indent + line for line in wrapped_message.split('\n'))
    
    # Apply color and return
    return f"{color}{indented_message}{colorama.Fore.RESET}"