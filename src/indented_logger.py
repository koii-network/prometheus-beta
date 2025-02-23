"""
Indented Logging Module

This module provides a flexible logging utility that supports message indentation.
"""

class IndentedLogger:
    """
    A logger that supports indentation for nested logging.
    
    Attributes:
        _current_indent (int): The current indentation level.
        _indent_char (str): Character used for indentation (default is space).
        _indent_size (int): Number of indent characters per indent level.
    """
    
    def __init__(self, indent_size=4, indent_char=' '):
        """
        Initialize the IndentedLogger.
        
        Args:
            indent_size (int, optional): Number of characters per indent level. Defaults to 4.
            indent_char (str, optional): Character used for indentation. Defaults to space.
        
        Raises:
            ValueError: If indent_size is negative or indent_char is empty.
        """
        if indent_size < 0:
            raise ValueError("Indent size must be non-negative")
        if not indent_char:
            raise ValueError("Indent character cannot be empty")
        
        self._current_indent = 0
        self._indent_size = indent_size
        self._indent_char = indent_char
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        Args:
            message (str): The message to log.
        
        Returns:
            str: The indented log message.
        """
        indent = self._indent_char * (self._current_indent * self._indent_size)
        return f"{indent}{message}"
    
    def indent(self):
        """
        Increase the indentation level by 1.
        """
        self._current_indent += 1
    
    def dedent(self):
        """
        Decrease the indentation level by 1.
        
        Raises:
            ValueError: If attempting to dedent below 0.
        """
        if self._current_indent > 0:
            self._current_indent -= 1
        else:
            raise ValueError("Cannot dedent below 0")
    
    def reset_indent(self):
        """
        Reset the indentation level to 0.
        """
        self._current_indent = 0
    
    def get_current_indent_level(self):
        """
        Get the current indentation level.
        
        Returns:
            int: The current indentation level.
        """
        return self._current_indent