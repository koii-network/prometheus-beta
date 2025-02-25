import os
import pytest
import logging
import tempfile
from unittest.mock import patch
from src.user_input_logger import log_user_input

def test_log_user_input_basic():
    """Test basic logging of user input."""
    with patch('builtins.input', return_value='test input'):
        result = log_user_input()
        assert result == 'test input'

def test_log_user_input_to_file():
    """Test logging user input to a file."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    try:
        with patch('builtins.input', return_value='file logging test'):
            log_user_input(log_file=temp_log_path)
        
        # Check log file contents
        with open(temp_log_path, 'r') as log_file:
            log_content = log_file.read()
            assert 'file logging test' in log_content
    finally:
        # Clean up the temporary file
        os.unlink(temp_log_path)

def test_log_user_input_empty_input():
    """Test that empty input raises a ValueError."""
    with patch('builtins.input', return_value='   '):
        with pytest.raises(ValueError, match="Input cannot be empty."):
            log_user_input()

def test_log_user_input_interrupt():
    """Test handling of input interruption."""
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            log_user_input()

def test_log_user_input_custom_log_level():
    """Test logging with a custom log level."""
    with patch('builtins.input', return_value='custom level test'):
        result = log_user_input(log_level=logging.DEBUG)
        assert result == 'custom level test'