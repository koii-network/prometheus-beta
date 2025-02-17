import os
import pytest
from src.timestamp_logger import log_with_timestamp

def test_log_with_timestamp():
    # Test basic logging
    log_file = 'test_app.log'
    message = "Test log message"
    result = log_with_timestamp(message, log_file)
    
    # Check the return value
    assert result.endswith(message)
    assert '[' in result and ']' in result
    
    # Check file contents
    with open(log_file, 'r') as f:
        log_content = f.read().strip()
        assert log_content.endswith(message)
    
    # Clean up test log file
    os.remove(log_file)

def test_log_invalid_input():
    # Test logging with non-string input
    with pytest.raises(TypeError):
        log_with_timestamp(123)

def test_log_file_creation():
    # Test that log file is created if it doesn't exist
    log_file = 'new_test_log.log'
    
    # Ensure file doesn't exist before test
    if os.path.exists(log_file):
        os.remove(log_file)
    
    log_with_timestamp("Test log", log_file)
    
    assert os.path.exists(log_file)
    
    # Clean up
    os.remove(log_file)

def test_multiple_logs():
    # Test logging multiple entries
    log_file = 'multiple_logs.log'
    messages = ["First log", "Second log", "Third log"]
    
    for msg in messages:
        log_with_timestamp(msg, log_file)
    
    # Check file contents
    with open(log_file, 'r') as f:
        log_lines = f.readlines()
        assert len(log_lines) == 3
        for line, msg in zip(log_lines, messages):
            assert msg in line
    
    # Clean up
    os.remove(log_file)