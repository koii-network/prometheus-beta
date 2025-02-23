import os
import pytest
import datetime
from src.timestamp_logger import log_with_timestamp

def test_log_with_timestamp_basic():
    """Test basic logging functionality"""
    test_log_file = 'logs/test_log.log'
    
    # Remove test log file if it exists
    if os.path.exists(test_log_file):
        os.remove(test_log_file)
    
    # Log a message
    result = log_with_timestamp("Test log message", test_log_file)
    
    # Check result format
    assert result.startswith(datetime.datetime.now().isoformat().split('T')[0])
    assert "Test log message" in result
    
    # Check file was created and contains the log
    with open(test_log_file, 'r') as f:
        log_content = f.read().strip()
        assert log_content == result

def test_log_with_timestamp_multiple_entries():
    """Test logging multiple entries"""
    test_log_file = 'logs/multi_log.log'
    
    # Remove test log file if it exists
    if os.path.exists(test_log_file):
        os.remove(test_log_file)
    
    # Log multiple messages
    log_with_timestamp("First message", test_log_file)
    log_with_timestamp("Second message", test_log_file)
    
    # Check file contents
    with open(test_log_file, 'r') as f:
        log_lines = f.readlines()
        assert len(log_lines) == 2
        assert "First message" in log_lines[0]
        assert "Second message" in log_lines[1]

def test_log_with_timestamp_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        log_with_timestamp(123)  # Non-string input
    
    with pytest.raises(TypeError):
        log_with_timestamp(None)  # None input

def test_log_with_timestamp_default_path():
    """Test logging with default path"""
    default_log_file = 'logs/app.log'
    
    # Remove default log file if it exists
    if os.path.exists(default_log_file):
        os.remove(default_log_file)
    
    # Log a message with default path
    log_with_timestamp("Default path message")
    
    # Verify file was created at default path
    assert os.path.exists(default_log_file)