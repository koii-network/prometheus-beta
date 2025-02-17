import logging
from typing import List, Any

class MenuLogger:
    """
    A class to log user selections from a menu.
    """
    def __init__(self, log_file: str = 'user_menu_selections.log'):
        """
        Initialize the MenuLogger with a specific log file.
        
        :param log_file: Path to the log file (default: 'user_menu_selections.log')
        """
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def log_selection(self, menu_name: str, selection: Any) -> None:
        """
        Log a user's menu selection.
        
        :param menu_name: Name or identifier of the menu
        :param selection: The item selected by the user
        """
        if not menu_name or selection is None:
            self.logger.warning("Invalid menu selection: menu_name and selection cannot be empty")
            return
        
        log_message = f"Menu: {menu_name} - Selected: {selection}"
        self.logger.info(log_message)
    
    def log_multiple_selections(self, menu_name: str, selections: List[Any]) -> None:
        """
        Log multiple selections from a menu.
        
        :param menu_name: Name or identifier of the menu
        :param selections: List of items selected by the user
        """
        if not menu_name or not selections:
            self.logger.warning("Invalid menu selections: menu_name and selections cannot be empty")
            return
        
        log_message = f"Menu: {menu_name} - Selections: {selections}"
        self.logger.info(log_message)