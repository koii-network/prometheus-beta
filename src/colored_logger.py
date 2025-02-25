from typing import Optional, Union, List

class BackgroundColorLogger:
    """
    A logger class that supports logging with background colors.
    """
    # ANSI color codes for background colors
    BACKGROUND_COLORS = {
        'black': '\033[40m',
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
    def log(
        cls, 
        message: str, 
        background_color: Optional[str] = None, 
        text_color: Optional[str] = None
    ) -> str:
        """
        Log a message with optional background and text colors.

        Args:
            message (str): The message to log
            background_color (Optional[str]): Background color (default: None)
            text_color (Optional[str]): Text color (default: None)

        Returns:
            str: The colored log message

        Raises:
            ValueError: If an invalid color is provided
        """
        # Validate background color
        if background_color and background_color.lower() not in cls.BACKGROUND_COLORS:
            raise ValueError(f"Invalid background color: {background_color}. "
                             f"Available colors are: {', '.join(cls.BACKGROUND_COLORS.keys())}")
        
        # Validate text color if provided
        text_color_map = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m'
        }
        
        if text_color and text_color.lower() not in text_color_map:
            raise ValueError(f"Invalid text color: {text_color}. "
                             f"Available colors are: {', '.join(text_color_map.keys())}")
        
        # Construct the colored message
        bg_code = cls.BACKGROUND_COLORS.get(background_color.lower(), '') if background_color else ''
        txt_code = text_color_map.get(text_color.lower(), '') if text_color else ''
        reset_code = cls.BACKGROUND_COLORS['reset']
        
        colored_message = f"{bg_code}{txt_code}{message}{reset_code}"
        
        # Print the message (optional, can be removed or modified as needed)
        print(colored_message)
        
        return colored_message