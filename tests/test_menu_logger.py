import os
import logging
import pytest
from src.menu_logger import MenuLogger

def test_single_selection_logging(tmp_path):
    """Test logging a single menu selection."""
    # Ensure unique file path for each test run
    log_file = str(tmp_path / "test_single_selection.log")
    
    # Create a new logger with a unique file path for each test run
    logger = MenuLogger(log_file=log_file)
    
    # Log a selection and allow logger to flush
    logger.log_selection("Main Menu", "Exit")
    
    # Create a new logger to flush any buffered data
    backup_logger = MenuLogger(log_file=log_file)
    
    # Verify log file contents by reading the actual file
    assert os.path.exists(log_file), "Log file was not created"
    
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert "Menu: Main Menu - Selected: Exit" in log_content

def test_multiple_selections_logging(tmp_path):
    """Test logging multiple menu selections."""
    # Ensure unique file path for each test run
    log_file = str(tmp_path / "test_multiple_selections.log")
    
    # Create a new logger with a unique file path for each test run
    logger = MenuLogger(log_file=log_file)
    
    selections = ["Option 1", "Option 2", "Option 3"]
    logger.log_multiple_selections("Settings Menu", selections)
    
    # Create a new logger to flush any buffered data
    backup_logger = MenuLogger(log_file=log_file)
    
    # Verify log file contents
    assert os.path.exists(log_file), "Log file was not created"
    
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    for selection in selections:
        assert f"Menu: Settings Menu - Selected: {selection}" in log_content

def test_empty_menu_name_raises_error():
    """Test that empty menu name raises a ValueError."""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_selection("", "Selection")
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_multiple_selections("", ["Selection"])

def test_none_selection_raises_error():
    """Test that None selection raises a ValueError."""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Selection cannot be None"):
        logger.log_selection("Menu", None)

def test_empty_selections_list_raises_error():
    """Test that empty selections list raises a ValueError."""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Selections list cannot be empty"):
        logger.log_multiple_selections("Menu", [])