import logging
from typing import List, Any

def log_user_selection(menu_items: List[str], selected_item: Any, log_file: str = 'user_selections.log') -> None:
    """
    Log user selections from a menu to a specified log file.
    
    Args:
        menu_items (List[str]): List of available menu items
        selected_item (Any): The item selected by the user
        log_file (str, optional): Path to the log file. Defaults to 'user_selections.log'.
    
    Raises:
        ValueError: If the selected item is not in the menu items
    """
    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - Menu Selection - %(message)s'
    )
    
    # Validate input
    if selected_item not in menu_items:
        raise ValueError(f"Selected item '{selected_item}' is not in the menu items")
    
    # Log the selection
    logging.info(f"User selected: {selected_item}")