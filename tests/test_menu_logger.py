import os
import logging
import pytest
from src.menu_logger import log_user_selection

def test_log_user_selection(tmp_path):
    # Prepare test data
    menu_items = ["Option 1", "Option 2", "Option 3"]
    selected_item = "Option 2"
    log_file = os.path.join(tmp_path, "test_selections.log")
    
    # Call the function
    log_user_selection(menu_items, selected_item, log_file)
    
    # Verify log file was created
    assert os.path.exists(log_file)
    
    # Read log file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    # Check log content
    assert "User selected: Option 2" in log_content

def test_log_user_selection_invalid_item():
    # Prepare test data
    menu_items = ["Option 1", "Option 2"]
    invalid_item = "Option 3"
    
    # Verify that an invalid item raises a ValueError
    with pytest.raises(ValueError, match=f"Selected item '{invalid_item}' is not in the menu items"):
        log_user_selection(menu_items, invalid_item)

def test_log_user_selection_empty_menu():
    # Verify behavior with an empty menu
    with pytest.raises(ValueError):
        log_user_selection([], "Some Item")