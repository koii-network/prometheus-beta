import sys

class IndentedLogger:
    def __init__(self, indent_char='  ', file=sys.stdout):
        """
        Initialize an IndentedLogger.
        
        :param indent_char: Character used for indentation (default is two spaces)
        :param file: File-like object to write logs to (default is sys.stdout)
        """
        self._current_indent = 0
        self._indent_char = indent_char
        self._file = file
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        :param message: Message to log
        """
        indented_message = self._indent_char * self._current_indent + str(message)
        print(indented_message, file=self._file)
    
    def indent(self):
        """
        Increase indentation level by 1.
        """
        self._current_indent += 1
    
    def dedent(self):
        """
        Decrease indentation level by 1, but not below 0.
        """
        self._current_indent = max(0, self._current_indent - 1)
    
    def reset_indent(self):
        """
        Reset indentation level to 0.
        """
        self._current_indent = 0