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

def log_with_background(message, background_color=None, file=sys.stdout):
    """
    Log a message with an optional background color.

    Args:
        message (str): The message to log.
        background_color (str, optional): Background color from BackgroundColors. 
            Defaults to None (no background color).
        file (file, optional): File-like object to write to. Defaults to sys.stdout.

    Raises:
        ValueError: If an invalid background color is provided.
        TypeError: If message is not a string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # If no background color, simply print the message
    if background_color is None:
        print(message, file=file)
        return

    # Validate background color
    valid_colors = [
        BackgroundColors.RED, 
        BackgroundColors.GREEN, 
        BackgroundColors.YELLOW, 
        BackgroundColors.BLUE, 
        BackgroundColors.MAGENTA, 
        BackgroundColors.CYAN, 
        BackgroundColors.WHITE
    ]
    if background_color not in valid_colors:
        raise ValueError(f"Invalid background color. Use colors from BackgroundColors class.")

    # Log message with background color
    try:
        print(f"{background_color}{message}{BackgroundColors.RESET}", file=file)
    except Exception as e:
        raise RuntimeError(f"Error logging message: {e}")