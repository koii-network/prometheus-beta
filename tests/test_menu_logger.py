import os
import logging
import pytest
from src.menu_logger import log_menu_selection

def test_log_menu_selection_valid_input(tmp_path):
    # Set up a temporary log file
    log_file = tmp_path / 'test_menu_selections.log'
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - Menu Selection - %(levelname)s: %(message)s',
        filename=str(log_file)
    )
    
    # Test menu items
    menu_items = ['Option 1', 'Option 2', 'Option 3']
    
    # Log a selection
    log_menu_selection(menu_items, 1)
    
    # Check log contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert 'User selected: \'Option 2\' at index 1' in log_content

def test_log_menu_selection_invalid_index():
    menu_items = ['Option 1', 'Option 2']
    
    with pytest.raises(ValueError, match="Selected index 2 is out of range"):
        log_menu_selection(menu_items, 2)
    
    with pytest.raises(ValueError, match="Selected index -1 is out of range"):
        log_menu_selection(menu_items, -1)

def test_log_menu_selection_empty_menu():
    with pytest.raises(ValueError, match="Menu items list cannot be empty"):
        log_menu_selection([], 0)

def test_log_menu_selection_invalid_input_type():
    with pytest.raises(TypeError, match="Menu items must be a list"):
        log_menu_selection("Not a list", 0)