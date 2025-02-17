import os
import logging
import pytest
from unittest.mock import patch
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.command_line_logger import log_user_input

def test_log_user_input_basic():
    # Prepare a log file for testing
    log_file = 'logs/user_input.log'
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Simulate user input
    with patch('builtins.input', return_value='test input'):
        result = log_user_input()
    
    # Check return value
    assert result == 'test input'
    
    # Check log file was created
    assert os.path.exists(log_file)
    
    # Check log file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'test input' in log_content

def test_log_user_input_error_handling():
    # Simulate an input error
    with patch('builtins.input', side_effect=Exception("Simulated input error")):
        result = log_user_input()
    
    # Check that None is returned on error
    assert result is None