import logging
from typing import List, Any

def log_user_selection(menu_items: List[str], selection: Any, log_file: str = 'user_selections.log') -> None:
    """
    Log user selections from a menu with detailed information.
    
    Args:
        menu_items (List[str]): List of available menu items
        selection (Any): The user's selected item
        log_file (str, optional): Path to the log file. Defaults to 'user_selections.log'
    
    Raises:
        ValueError: If the selection is not in the menu items
    """
    # Configure logging to write to the specified file
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - Menu Selection - %(message)s'
    )
    
    # Validate the selection
    if selection not in menu_items:
        logging.error(f"Invalid selection: {selection}. Not in menu items: {menu_items}")
        raise ValueError(f"Selection '{selection}' is not a valid menu item")
    
    # Log the successful selection
    logging.info(f"User selected: {selection}")
    
    return None