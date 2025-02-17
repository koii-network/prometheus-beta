import colorama
from typing import Optional, Literal

class CustomLogger:
    """
    A custom logger class that provides styled logging with color and formatting options.
    """
    
    def __init__(self):
        # Initialize colorama for cross-platform color support
        colorama.init(autoreset=True)
    
    def log(
        self, 
        message: str, 
        level: Literal["info", "warning", "error", "success"] = "info", 
        prefix: Optional[str] = None
    ) -> str:
        """
        Log a message with custom styling based on the log level.
        
        Args:
            message (str): The message to log
            level (str, optional): The log level. Defaults to "info".
            prefix (str, optional): A custom prefix for the log message. Defaults to None.
        
        Returns:
            str: The formatted log message
        """
        # Define color mappings
        color_map = {
            "info": colorama.Fore.BLUE,
            "warning": colorama.Fore.YELLOW,
            "error": colorama.Fore.RED,
            "success": colorama.Fore.GREEN
        }
        
        # Validate level
        if level not in color_map:
            raise ValueError(f"Invalid log level. Must be one of {list(color_map.keys())}")
        
        # Determine color and prefix
        color = color_map[level]
        log_prefix = prefix or level.upper()
        
        # Format the log message
        formatted_message = f"{color}[{log_prefix}] {message}"
        
        # Print the message (for console output)
        print(formatted_message)
        
        # Return the formatted message for potential further processing
        return formatted_message