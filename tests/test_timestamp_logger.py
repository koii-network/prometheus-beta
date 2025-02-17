import os
import pytest
from src.timestamp_logger import log_with_timestamp

def test_log_with_timestamp(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / 'test.log'
    
    # Log a message
    message = "Test log message"
    result = log_with_timestamp(message, str(log_file))
    
    # Check log file contents
    with open(log_file, 'r') as f:
        log_contents = f.read().strip()
    
    # Verify the logged message has a timestamp
    assert log_contents.startswith('[')
    assert ']' in log_contents
    assert message in log_contents
    
    # Verify the function returns the log entry
    assert log_contents == result

def test_log_with_default_filename(tmp_path):
    # Change current working directory
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    try:
        # Log a message using default filename
        message = "Default log test"
        result = log_with_timestamp(message)
        
        # Check default log file contents
        with open('app.log', 'r') as f:
            log_contents = f.read().strip()
        
        # Verify the logged message
        assert log_contents.startswith('[')
        assert ']' in log_contents
        assert message in log_contents
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

def test_multiple_logs(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / 'multiple_logs.log'
    
    # Log multiple messages
    messages = ["First log", "Second log", "Third log"]
    for msg in messages:
        log_with_timestamp(msg, str(log_file))
    
    # Check log file contents
    with open(log_file, 'r') as f:
        log_contents = f.readlines()
    
    # Verify multiple logs are added
    assert len(log_contents) == 3
    for i, line in enumerate(log_contents):
        assert messages[i] in line