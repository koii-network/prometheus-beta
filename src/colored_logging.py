import sys

class BackgroundColors:
    """Enum-like class for background color codes."""
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[0m'

def log_with_background(message, color=BackgroundColors.WHITE, file=sys.stdout):
    """
    Log a message with a specified background color.
    
    Args:
        message (str): The message to log
        color (str, optional): Background color from BackgroundColors. Defaults to WHITE.
        file (file-like object, optional): Output stream. Defaults to sys.stdout.
    
    Raises:
        ValueError: If the color is not a valid background color
        TypeError: If message is not a string
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Validate color
    valid_colors = [
        BackgroundColors.RED, BackgroundColors.GREEN, BackgroundColors.YELLOW,
        BackgroundColors.BLUE, BackgroundColors.MAGENTA, BackgroundColors.CYAN,
        BackgroundColors.WHITE
    ]
    if color not in valid_colors:
        raise ValueError("Invalid background color")
    
    # Log the message with the specified background color
    colored_message = f"{color}{message}{BackgroundColors.RESET}"
    print(colored_message, file=file)