import os
import pytest
import logging
from unittest.mock import patch
from src.user_input_logger import log_user_input

def get_log_path():
    """Get the absolute path to the log file."""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'user_input.log')

def test_log_user_input_success():
    # Ensure log file doesn't exist before test
    log_path = get_log_path()
    if os.path.exists(log_path):
        os.remove(log_path)
    
    # Simulate user input
    with patch('builtins.input', return_value="Test input"):
        with patch('builtins.print'):  # Suppress print output
            result = log_user_input()
    
    # Check return value
    assert result == "Test input"
    
    # Check log file contents
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "User input: Test input" in log_content

def test_log_user_input_empty():
    # Ensure log file doesn't exist before test
    log_path = get_log_path()
    if os.path.exists(log_path):
        os.remove(log_path)
    
    # Simulate empty input
    with patch('builtins.input', return_value=""):
        with patch('builtins.print'):  # Suppress print output
            result = log_user_input()
    
    # Check return value
    assert result == ""
    
    # Check log file contents
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "Empty input received" in log_content

def test_log_user_input_exception():
    # Simulate input with exception
    with patch('builtins.input', side_effect=Exception("Test exception")):
        with pytest.raises(Exception):
            log_user_input()