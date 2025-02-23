import logging
import os
import sys
from typing import List, Union

class MenuLogger:
    """
    A class to log user menu selections with configurable logging options.
    """
    
    def __init__(self, log_file: str = 'menu_selections.log', log_level: int = logging.INFO):
        """
        Initialize the MenuLogger with specified log file and logging level.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'menu_selections.log'.
            log_level (int, optional): Logging level. Defaults to logging.INFO.
        """
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Create a unique logger name to prevent handler conflicts
        logger_name = f'menu_logger_{hash(log_file)}'
        
        # Create logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        
        # Remove existing handlers to prevent duplicate logging
        while self.logger.handlers:
            self.logger.removeHandler(self.logger.handlers[0])
        
        # Create file handler
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        
        # Add handler to logger
        self.logger.addHandler(file_handler)
        
        # Prevent handler propagation to root logger
        self.logger.propagate = False
    
    def log_selection(self, menu_name: str, selection: Union[str, int]) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Union[str, int]): The selected item from the menu.
        
        Raises:
            ValueError: If menu_name is empty or selection is None.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if selection is None:
            raise ValueError("Selection cannot be None")
        
        # Log the selection
        log_message = f"Menu: {menu_name} - Selected: {selection}"
        self.logger.info(log_message)
        
        # Ensure immediate writing
        for handler in self.logger.handlers:
            handler.flush()
    
    def log_multiple_selections(self, menu_name: str, selections: List[Union[str, int]]) -> None:
        """
        Log multiple selections from a menu.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selections (List[Union[str, int]]): List of selected items.
        
        Raises:
            ValueError: If menu_name is empty or selections list is empty.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if not selections:
            raise ValueError("Selections list cannot be empty")
        
        # Log multiple selections
        for selection in selections:
            self.log_selection(menu_name, selection)