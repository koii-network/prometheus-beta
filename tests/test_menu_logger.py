import os
import logging
import pytest
from src.menu_logger import log_user_selection

def test_valid_selection(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "test_selection.log"
    
    # Setup menu items
    menu_items = ["Option 1", "Option 2", "Option 3"]
    selection = "Option 2"
    
    # Call the function
    log_user_selection(menu_items, selection, str(log_file))
    
    # Check log contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert "User selected: Option 2" in log_content

def test_invalid_selection():
    # Setup menu items
    menu_items = ["Option 1", "Option 2", "Option 3"]
    invalid_selection = "Option 4"
    
    # Expect a ValueError
    with pytest.raises(ValueError, match=f"Selection 'Option 4' is not a valid menu item"):
        log_user_selection(menu_items, invalid_selection)

def test_empty_menu_items():
    # Test with an empty menu
    with pytest.raises(ValueError, match="Selection .* is not a valid menu item"):
        log_user_selection([], "Any Selection")

def test_different_types_of_selections():
    # Test with different types of menu items and selections
    menu_items = [1, 2, 3, "four"]
    
    # Test integer selection
    log_user_selection(menu_items, 2)
    
    # Test string selection
    log_user_selection(menu_items, "four")
    
    # Test invalid selection
    with pytest.raises(ValueError):
        log_user_selection(menu_items, 5)