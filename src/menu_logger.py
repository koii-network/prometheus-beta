import logging
from typing import List, Any

def log_menu_selection(menu_items: List[str], selected_index: int) -> None:
    """
    Log the user's menu selection with appropriate logging levels.
    
    Args:
        menu_items (List[str]): A list of menu items 
        selected_index (int): The index of the selected menu item
    
    Raises:
        ValueError: If the selected index is out of range
    """
    # Configure logging 
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - Menu Selection - %(levelname)s: %(message)s',
        filename='menu_selections.log'
    )
    
    # Validate input
    if not isinstance(menu_items, list):
        raise TypeError("Menu items must be a list")
    
    if not menu_items:
        raise ValueError("Menu items list cannot be empty")
    
    # Check if selected index is valid
    if selected_index < 0 or selected_index >= len(menu_items):
        raise ValueError(f"Selected index {selected_index} is out of range. "
                         f"Valid range is 0 to {len(menu_items) - 1}")
    
    # Log the selection
    selected_item = menu_items[selected_index]
    logging.info(f"User selected: '{selected_item}' at index {selected_index}")