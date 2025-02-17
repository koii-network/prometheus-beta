class IndentedLogger:
    def __init__(self, initial_indent=0, indent_step=2):
        """
        Initialize an IndentedLogger with configurable indentation.
        
        :param initial_indent: Starting indentation level (default 0)
        :param indent_step: Number of spaces per indentation level (default 2)
        """
        self._current_indent = initial_indent
        self._indent_step = indent_step
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        :param message: Message to log
        :return: Indented log message
        """
        indentation = ' ' * (self._current_indent * self._indent_step)
        print(f"{indentation}{message}")
        return f"{indentation}{message}"
    
    def indent(self):
        """
        Increase indentation level by one step.
        """
        self._current_indent += 1
    
    def dedent(self):
        """
        Decrease indentation level by one step, ensuring it doesn't go below 0.
        """
        self._current_indent = max(0, self._current_indent - 1)
    
    def reset_indent(self):
        """
        Reset indentation to initial level.
        """
        self._current_indent = 0