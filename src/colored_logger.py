import sys

class ColoredLogger:
    """
    A logger class that provides colored output to console with background color support.
    """
    # ANSI color codes for background colors
    BACKGROUND_COLORS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'default': '\033[49m'
    }

    # ANSI text color codes
    TEXT_COLORS = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    @classmethod
    def log(cls, message, bg_color='default', text_color='white', file=sys.stdout):
        """
        Log a message with specified background and text colors.
        
        Args:
            message (str): The message to log
            bg_color (str, optional): Background color. Defaults to 'default'.
            text_color (str, optional): Text color. Defaults to 'white'.
            file (file, optional): Output file stream. Defaults to sys.stdout.
        
        Raises:
            ValueError: If an invalid color is provided
        """
        # Validate background color
        if bg_color not in cls.BACKGROUND_COLORS:
            raise ValueError(f"Invalid background color. Choose from {list(cls.BACKGROUND_COLORS.keys())}")
        
        # Validate text color
        if text_color not in cls.TEXT_COLORS and text_color != 'reset':
            raise ValueError(f"Invalid text color. Choose from {list(cls.TEXT_COLORS.keys())}")
        
        # Construct the colored output
        bg = cls.BACKGROUND_COLORS[bg_color]
        text = cls.TEXT_COLORS[text_color] if text_color != 'reset' else cls.TEXT_COLORS['reset']
        reset = cls.TEXT_COLORS['reset']
        
        # Print the colored message
        print(f"{bg}{text}{message}{reset}", file=file)