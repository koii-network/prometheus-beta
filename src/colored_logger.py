import sys

class ColoredLogger:
    """
    A logger class that supports colored background logging to console.
    """
    # ANSI escape codes for background colors
    BACKGROUNDS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m'
    }
    
    # Reset to default terminal color
    RESET = '\033[0m'

    @classmethod
    def log(cls, message, bg_color='white', text_color=None, file=sys.stdout):
        """
        Log a message with specified background color.
        
        Args:
            message (str): The message to log
            bg_color (str, optional): Background color. Defaults to 'white'.
            text_color (str, optional): Text color. Defaults to None (automatic contrast).
            file (file, optional): Output stream. Defaults to sys.stdout.
        
        Raises:
            ValueError: If an invalid background color is specified
        """
        # Validate background color
        if bg_color not in cls.BACKGROUNDS:
            raise ValueError(f"Invalid background color. Choose from {list(cls.BACKGROUNDS.keys())}")
        
        # Determine text color for readability
        if text_color is None:
            text_color = 'black' if bg_color in ['yellow', 'white', 'cyan'] else 'white'
        
        # Create ANSI color code
        bg_code = cls.BACKGROUNDS[bg_color]
        text_code = f'\033[{30 if text_color == "black" else 37}m'
        
        # Format and print colored message
        colored_message = f"{bg_code}{text_code}{message}{cls.RESET}"
        print(colored_message, file=file)