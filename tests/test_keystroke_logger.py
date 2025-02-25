import os
import logging
import pytest
import tempfile

from src.keystroke_logger import KeystrokeLogger

def test_keystroke_logger_basic_logging():
    """Test basic keystroke logging functionality."""
    logger = KeystrokeLogger()
    
    # Log some keystrokes
    test_keys = ['a', 'b', 'c']
    for key in test_keys:
        logger.log_keystroke(key)
    
    # Check buffer contents
    assert logger.get_keystroke_buffer() == test_keys

def test_keystroke_logger_file_logging():
    """Test logging keystrokes to a file."""
    # Create a temporary file for logging
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.log') as temp_log:
        temp_log_path = temp_log.name
    
    try:
        # Create logger with file output
        logger = KeystrokeLogger(log_file=temp_log_path)
        
        # Log some keystrokes
        test_keys = ['x', 'y', 'z']
        for key in test_keys:
            logger.log_keystroke(key)
        
        # Read log file contents
        with open(temp_log_path, 'r') as log_file:
            log_contents = log_file.read()
        
        # Verify log contents
        for key in test_keys:
            assert f"Keystroke: {key}" in log_contents
    
    finally:
        # Clean up temporary file
        os.unlink(temp_log_path)

def test_keystroke_logger_invalid_input():
    """Test error handling for invalid keystroke inputs."""
    logger = KeystrokeLogger()
    
    # Test multiple characters
    with pytest.raises(ValueError, match="Keystroke must be a single character"):
        logger.log_keystroke("ab")
    
    # Test empty string
    with pytest.raises(ValueError, match="Keystroke must be a single character"):
        logger.log_keystroke("")
    
    # Test non-string input
    with pytest.raises(ValueError, match="Keystroke must be a single character"):
        logger.log_keystroke(123)

def test_keystroke_logger_buffer_management():
    """Test buffer clearing functionality."""
    logger = KeystrokeLogger()
    
    # Log some keystrokes
    test_keys = ['1', '2', '3']
    for key in test_keys:
        logger.log_keystroke(key)
    
    # Verify buffer contents
    assert logger.get_keystroke_buffer() == test_keys
    
    # Clear buffer
    logger.clear_keystroke_buffer()
    
    # Verify buffer is empty
    assert logger.get_keystroke_buffer() == []

def test_keystroke_logger_log_level():
    """Test custom log level configuration."""
    # Create a temporary file for logging
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.log') as temp_log:
        temp_log_path = temp_log.name
    
    try:
        # Create logger with DEBUG level
        logger = KeystrokeLogger(log_file=temp_log_path, log_level=logging.DEBUG)
        
        # Log a keystroke
        logger.log_keystroke('d')
        
        # Read log file contents
        with open(temp_log_path, 'r') as log_file:
            log_contents = log_file.read()
        
        # Verify log entry exists
        assert "Keystroke: d" in log_contents
    
    finally:
        # Clean up temporary file
        os.unlink(temp_log_path)