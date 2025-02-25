import logging
import os
from typing import List, Union

class MenuLogger:
    """
    A class to handle logging of user menu selections.
    
    This logger provides methods to log menu selections with different 
    logging levels and optional additional context.
    """
    
    def __init__(self, log_file: str = 'menu_selections.log', log_level: int = logging.INFO):
        """
        Initialize the MenuLogger.
        
        :param log_file: Path to the log file (default: 'menu_selections.log')
        :param log_level: Logging level (default: logging.INFO)
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Create a file handler
        self.log_file = log_file
        self.handler = logging.FileHandler(filename=log_file, mode='a')
        self.handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        
        # Create a logger
        self.logger = logging.getLogger(f'menu_logger_{os.getpid()}')
        self.logger.setLevel(log_level)
        
        # Add the handler to the logger (remove any existing handlers first)
        self.logger.handlers.clear()
        self.logger.addHandler(self.handler)
        
        # Prevent propagation to root logger
        self.logger.propagate = False
    
    def __del__(self):
        """
        Ensure the file handler is closed when the object is deleted.
        """
        if hasattr(self, 'handler'):
            self.handler.close()
    
    def log_selection(self, 
                      selection: Union[str, int], 
                      menu_name: str = 'Default Menu', 
                      additional_context: dict = None) -> None:
        """
        Log a user's menu selection.
        
        :param selection: The selected menu item (can be string or integer)
        :param menu_name: Name of the menu (optional)
        :param additional_context: Optional dictionary of additional contextual information
        :raises ValueError: If selection is None or empty
        """
        # Validate input
        if selection is None:
            raise ValueError("Selection cannot be None")
        
        # Prepare log message
        log_message = f"Menu: {menu_name}, Selection: {selection}"
        
        # Add additional context if provided
        if additional_context:
            context_str = ', '.join(f"{k}: {v}" for k, v in additional_context.items())
            log_message += f" (Context: {context_str})"
        
        # Log the selection with direct write (as a fallback)
        try:
            self.logger.info(log_message)
            self.handler.flush()
        except Exception:
            # Fallback direct file write
            try:
                with open(self.log_file, 'a') as f:
                    f.write(f'{log_message}\n')
            except Exception:
                pass
    
    def log_invalid_selection(self, 
                               invalid_selection: Union[str, int], 
                               menu_name: str = 'Default Menu') -> None:
        """
        Log an invalid menu selection.
        
        :param invalid_selection: The invalid selection attempted
        :param menu_name: Name of the menu (optional)
        """
        log_message = f"Invalid Selection - Menu: {menu_name}, Attempted Selection: {invalid_selection}"
        
        # Log the invalid selection with direct write (as a fallback)
        try:
            self.logger.warning(log_message)
            self.handler.flush()
        except Exception:
            # Fallback direct file write
            try:
                with open(self.log_file, 'a') as f:
                    f.write(f'{log_message}\n')
            except Exception:
                pass