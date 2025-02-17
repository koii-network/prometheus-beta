import colorama
from typing import Optional, Literal

# Initialize colorama for cross-platform color support
colorama.init(autoreset=True)

def log_with_style(
    message: str, 
    style: Optional[Literal['success', 'warning', 'error', 'info']] = None, 
    prefix: Optional[str] = None
) -> str:
    """
    Log a message with custom styling and optional prefix.
    
    Args:
        message (str): The message to log
        style (Optional[str]): Style of the message (success, warning, error, info)
        prefix (Optional[str]): Optional custom prefix for the message
    
    Returns:
        str: Formatted and styled log message
    """
    # Define color and prefix mappings
    styles = {
        'success': colorama.Fore.GREEN,
        'warning': colorama.Fore.YELLOW,
        'error': colorama.Fore.RED,
        'info': colorama.Fore.BLUE
    }
    
    # Default to info if no style is provided
    color = styles.get(style, colorama.Fore.WHITE)
    
    # Construct the prefix
    log_prefix = f"[{style.upper()}] " if style else ""
    if prefix:
        log_prefix = f"[{prefix}] "
    
    # Format the final message
    formatted_message = f"{color}{log_prefix}{message}{colorama.Fore.RESET}"
    
    # Print the message (optional, depending on logging requirements)
    print(formatted_message)
    
    return formatted_message