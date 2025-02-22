import logging
import os
from typing import Any, List

def log_user_selection(menu_name: str, selection: Any, log_file: str = 'user_menu_selections.log') -> None:
    """
    Log user selections from a menu to a specified log file.
    
    Args:
        menu_name (str): Name or identifier of the menu
        selection (Any): The user's selected item
        log_file (str, optional): Path to the log file. Defaults to 'user_menu_selections.log'
    
    Raises:
        ValueError: If menu_name is empty or selection is None
    """
    # Validate inputs
    if not menu_name:
        raise ValueError("Menu name cannot be empty")
    
    if selection is None:
        raise ValueError("Selection cannot be None")
    
    # Ensure log directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - Menu: %(menu)s - Selection: %(selection)s'
    )
    
    # Create a logger with extra context
    logger = logging.LoggerAdapter(
        logging.getLogger(__name__),
        {'menu': menu_name, 'selection': str(selection)}
    )
    
    # Log the user selection
    logger.info("User made a selection")