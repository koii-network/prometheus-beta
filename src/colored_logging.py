import sys

class BackgroundColors:
    """Defines ANSI background color codes for terminal logging."""
    RESET = '\033[49m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'

def log_with_background(message, color=BackgroundColors.WHITE, file=sys.stdout):
    """
    Log a message with a specified background color to the given file stream.
    
    Args:
        message (str): The message to log
        color (str, optional): Background color from BackgroundColors. Defaults to WHITE.
        file (file, optional): Output stream. Defaults to sys.stdout.
    
    Raises:
        TypeError: If message is not a string
        ValueError: If an invalid color is provided
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Validate color is from BackgroundColors
    valid_colors = [getattr(BackgroundColors, attr) for attr in dir(BackgroundColors) if not attr.startswith('__')]
    if color not in valid_colors:
        raise ValueError(f"Invalid color. Use colors from BackgroundColors class.")
    
    # Log message with background color
    colored_message = f"{color}{message}{BackgroundColors.RESET}"
    print(colored_message, file=file)