import sys

class BackgroundColorLogger:
    """
    A logger class that provides methods to print output with background colors.
    
    Supports ANSI color codes for terminal output with optional background coloring.
    """
    
    # ANSI color code constants
    COLORS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'reset': '\033[0m'
    }
    
    @classmethod
    def log(cls, message, bg_color=None, text_color=None, file=sys.stdout, end='\n'):
        """
        Log a message with optional background and text colors.
        
        Args:
            message (str): The message to log
            bg_color (str, optional): Background color. Defaults to None.
            text_color (str, optional): Text color. Defaults to None.
            file (file, optional): File-like object to write to. Defaults to sys.stdout.
            end (str, optional): String appended after the end of the message. Defaults to '\n'.
        
        Raises:
            ValueError: If an invalid color is provided
        """
        # Validate colors
        if bg_color and bg_color not in cls.COLORS:
            raise ValueError(f"Invalid background color: {bg_color}. Choose from {list(cls.COLORS.keys())}")
        
        # Construct color formatting
        bg_code = cls.COLORS.get(bg_color, '')
        reset_code = cls.COLORS['reset']
        
        # Apply formatting and print
        formatted_message = f"{bg_code}{message}{reset_code}"
        print(formatted_message, file=file, end=end)
    
    @classmethod
    def color_text(cls, message, text_color):
        """
        Color only the text (not the background).
        
        Args:
            message (str): The message to color
            text_color (str): Color of the text
        
        Returns:
            str: Colored text
        
        Raises:
            ValueError: If an invalid color is provided
        """
        # This would require additional ANSI codes for text coloring
        # Placeholder for future implementation
        raise NotImplementedError("Text color formatting not yet implemented")