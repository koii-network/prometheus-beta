class ColoredLogger:
    """A logger class that supports background color logging."""
    
    # ANSI escape codes for background colors
    BACKGROUND_COLORS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m'
    }
    
    # Reset color code
    RESET = '\033[0m'
    
    @classmethod
    def log(cls, message, background_color=None, text_color=None):
        """
        Log a message with optional background and text colors.
        
        Args:
            message (str): The message to log
            background_color (str, optional): Background color name
            text_color (str, optional): Text color name (not implemented in this version)
        
        Raises:
            ValueError: If an invalid background color is specified
        """
        # Validate background color
        if background_color and background_color.lower() not in cls.BACKGROUND_COLORS:
            raise ValueError(f"Invalid background color. Choose from: {', '.join(cls.BACKGROUND_COLORS.keys())}")
        
        # Apply background color if specified
        if background_color:
            colored_message = f"{cls.BACKGROUND_COLORS[background_color.lower()]}{message}{cls.RESET}"
            print(colored_message)
        else:
            print(message)