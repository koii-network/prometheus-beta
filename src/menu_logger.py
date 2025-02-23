import logging
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
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=log_level, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
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