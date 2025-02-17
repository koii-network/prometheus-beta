import os
import pytest
import logging
from unittest.mock import patch, mock_open
from src.user_input_logger import log_user_input

def get_log_path():
    """Get the absolute path to the log file."""
    return '/app/repos/repo_11/user_input.log'

def test_log_user_input_success():
    # Simulate user input
    with patch('builtins.input', return_value="Test input"), \
         patch('builtins.print'), \
         patch('logging.basicConfig'), \
         patch('logging.info') as mock_log_info:
        
        result = log_user_input()
    
    # Check return value
    assert result == "Test input"
    
    # Check logging
    mock_log_info.assert_called_once_with("User input: Test input")

def test_log_user_input_empty():
    # Simulate empty input
    with patch('builtins.input', return_value=""), \
         patch('builtins.print'), \
         patch('logging.basicConfig'), \
         patch('logging.warning') as mock_log_warning:
        
        result = log_user_input()
    
    # Check return value
    assert result == ""
    
    # Check logging
    mock_log_warning.assert_called_once_with("Empty input received")

def test_log_user_input_exception():
    # Simulate input with exception
    with patch('builtins.input', side_effect=Exception("Test exception")), \
         patch('logging.error') as mock_log_error:
        
        with pytest.raises(Exception):
            log_user_input()
        
        # Verify error was logged
        mock_log_error.assert_called_once()