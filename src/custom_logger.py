import colorama
from typing import Optional, Literal

class CustomLogger:
    """
    A custom logger class that provides styled logging capabilities.
    
    Supports different color and style options for logging messages.
    """
    
    # Initialize colorama for cross-platform color support
    colorama.init(autoreset=True)
    
    # Color and style mapping
    COLORS = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'blue': colorama.Fore.BLUE,
        'magenta': colorama.Fore.MAGENTA,
        'cyan': colorama.Fore.CYAN,
        'white': colorama.Fore.WHITE
    }
    
    STYLES = {
        'bright': colorama.Style.BRIGHT,
        'dim': colorama.Style.DIM,
        'normal': colorama.Style.NORMAL
    }
    
    @classmethod
    def log(
        cls, 
        message: str, 
        color: Optional[Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']] = None,
        style: Optional[Literal['bright', 'dim', 'normal']] = None,
        prefix: Optional[str] = None
    ) -> str:
        """
        Log a message with optional color and style customization.
        
        Args:
            message (str): The message to log
            color (Optional[str]): Color of the message
            style (Optional[str]): Style of the message
            prefix (Optional[str]): Optional prefix for the message
        
        Returns:
            str: The formatted log message
        
        Raises:
            ValueError: If an invalid color or style is provided
        """
        # Validate color and style inputs
        if color and color not in cls.COLORS:
            raise ValueError(f"Invalid color. Choose from {', '.join(cls.COLORS.keys())}")
        
        if style and style not in cls.STYLES:
            raise ValueError(f"Invalid style. Choose from {', '.join(cls.STYLES.keys())}")
        
        # Construct the log message
        formatted_message = message
        
        # Apply color if specified
        if color:
            formatted_message = f"{cls.COLORS[color]}{formatted_message}"
        
        # Apply style if specified
        if style:
            formatted_message = f"{cls.STYLES[style]}{formatted_message}"
        
        # Add prefix if specified
        if prefix:
            formatted_message = f"{prefix} {formatted_message}"
        
        # Print the message (for actual logging)
        print(formatted_message)
        
        return formatted_message