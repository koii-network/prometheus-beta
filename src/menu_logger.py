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
        
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=log_level, 
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='a'  # Append mode to preserve previous logs
        )
        self.logger = logging.getLogger(__name__)
    
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
        
        # Log the selection
        self.logger.info(log_message)
    
    def log_invalid_selection(self, 
                               invalid_selection: Union[str, int], 
                               menu_name: str = 'Default Menu') -> None:
        """
        Log an invalid menu selection.
        
        :param invalid_selection: The invalid selection attempted
        :param menu_name: Name of the menu (optional)
        """
        log_message = f"Invalid Selection - Menu: {menu_name}, Attempted Selection: {invalid_selection}"
        self.logger.warning(log_message)