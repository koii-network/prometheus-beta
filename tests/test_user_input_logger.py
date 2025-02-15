import os
import logging
import pytest
from unittest.mock import patch
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from user_input_logger import log_user_input

def test_log_user_input(tmp_path):
    # Setup logging to a temporary file
    log_file = tmp_path / "test_user_input.log"
    logging.basicConfig(
        filename=str(log_file), 
        level=logging.INFO, 
        format='%(asctime)s - %(message)s'
    )

    # Simulate user input
    with patch('builtins.input', return_value="test input"):
        result = log_user_input()
    
    # Check the return value
    assert result == "test input"

    # Check the log file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "User input: test input" in log_content

def test_log_user_input_error_handling():
    # Test error handling by forcing an exception
    with patch('builtins.input', side_effect=ValueError("Test error")):
        with pytest.raises(ValueError):
            log_user_input()