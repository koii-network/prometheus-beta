class IndentedLogger:
    def __init__(self, initial_indent=0, indent_step=2):
        """
        Initialize an IndentedLogger with optional initial indentation and indent step.
        
        :param initial_indent: Starting indentation level (default 0)
        :param indent_step: Number of spaces per indentation level (default 2)
        """
        self._current_indent = initial_indent
        self._indent_step = indent_step
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        :param message: Message to log
        :return: Indented message string
        """
        if not isinstance(message, str):
            message = str(message)
        
        indented_message = " " * (self._current_indent * self._indent_step) + message
        print(indented_message)
        return indented_message
    
    def indent(self, levels=1):
        """
        Increase indentation level.
        
        :param levels: Number of indentation levels to increase (default 1)
        """
        self._current_indent = max(0, self._current_indent + levels)
    
    def dedent(self, levels=1):
        """
        Decrease indentation level.
        
        :param levels: Number of indentation levels to decrease (default 1)
        """
        self._current_indent = max(0, self._current_indent - levels)
    
    def reset_indent(self):
        """
        Reset indentation to initial level.
        """
        self._current_indent = 0