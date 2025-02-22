import os
import logging
import pytest
from unittest.mock import patch
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from user_input_logger import log_user_input

def test_log_user_input_success(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "test_user_input.log"
    
    # Patch logging to use the temporary log file
    with patch('logging.basicConfig') as mock_config, \
         patch('builtins.input', return_value="test input"), \
         patch('logging.info') as mock_log_info:
        
        # Call the function
        result = log_user_input()
        
        # Assertions
        assert result == "test input"
        mock_log_info.assert_called_once_with("User input: test input")

def test_log_user_input_empty_input():
    # Test with empty input
    with patch('builtins.input', return_value=""), \
         patch('logging.info') as mock_log_info:
        
        result = log_user_input()
        
        assert result == ""
        mock_log_info.assert_called_once_with("User input: ")

def test_log_user_input_exception():
    # Test error handling
    with patch('builtins.input', side_effect=Exception("Test error")), \
         patch('logging.error') as mock_log_error:
        
        with pytest.raises(Exception, match="Test error"):
            log_user_input()
        
        mock_log_error.assert_called_once()