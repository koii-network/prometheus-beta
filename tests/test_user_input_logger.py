import pytest
import logging
import os
import tempfile
from unittest.mock import patch
from src.user_input_logger import log_user_input

def test_log_user_input_default():
    """Test logging with default parameters"""
    with patch('builtins.input', return_value="Test message"):
        result = log_user_input()
        assert result == "Test message"

def test_log_user_input_custom_level():
    """Test logging with a custom log level"""
    with patch('builtins.input', return_value="Debug message"):
        result = log_user_input(log_level='DEBUG')
        assert result == "Debug message"

def test_log_user_input_with_file():
    """Test logging to a file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    try:
        with patch('builtins.input', return_value="File log message"):
            result = log_user_input(log_level='INFO', log_file=temp_log_path)
        
        # Verify the log file contains the message
        with open(temp_log_path, 'r') as log_file:
            log_content = log_file.read()
            assert "File log message" in log_content
            assert result == "File log message"
    finally:
        # Clean up the temporary file
        os.unlink(temp_log_path)

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match='Invalid log level'):
        log_user_input(log_level='INVALID_LEVEL')

def test_log_user_input_interrupt():
    """Test handling of keyboard interrupt"""
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        result = log_user_input()
        assert result == ""