"""
A module for logging messages with indentation support.
"""

class IndentedLogger:
    """
    A logger that supports message indentation and log levels.
    
    Attributes:
        _indent_level (int): Current indentation level
        _indent_char (str): Character used for indentation (default is space)
        _indent_size (int): Number of indent characters per level (default is 4)
    """
    
    def __init__(self, indent_char=' ', indent_size=4):
        """
        Initialize the IndentedLogger.
        
        Args:
            indent_char (str, optional): Character used for indentation. Defaults to space.
            indent_size (int, optional): Number of indent characters per level. Defaults to 4.
        
        Raises:
            ValueError: If indent_size is negative.
        """
        if indent_size < 0:
            raise ValueError("Indent size must be non-negative")
        
        self._indent_level = 0
        self._indent_char = indent_char
        self._indent_size = indent_size
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        Args:
            message (str): The message to log
        
        Returns:
            str: The indented log message
        """
        if message is None:
            return ''
        
        indent = self._indent_char * (self._indent_level * self._indent_size)
        return f"{indent}{message}"
    
    def indent(self, levels=1):
        """
        Increase the indentation level.
        
        Args:
            levels (int, optional): Number of levels to increase. Defaults to 1.
        
        Raises:
            ValueError: If levels is negative.
        """
        if levels < 0:
            raise ValueError("Cannot indent by a negative number of levels")
        
        self._indent_level += levels
    
    def dedent(self, levels=1):
        """
        Decrease the indentation level.
        
        Args:
            levels (int, optional): Number of levels to decrease. Defaults to 1.
        
        Raises:
            ValueError: If levels is negative or would result in negative indentation.
        """
        if levels < 0:
            raise ValueError("Cannot dedent by a negative number of levels")
        
        self._indent_level = max(0, self._indent_level - levels)
    
    def get_indent_level(self):
        """
        Get the current indentation level.
        
        Returns:
            int: Current indentation level
        """
        return self._indent_level