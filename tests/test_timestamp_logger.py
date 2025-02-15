import os
import pytest
from src.timestamp_logger import log_with_timestamp
import datetime

def test_log_with_timestamp(tmp_path):
    # Create a temporary log file
    log_file = str(tmp_path / 'test.log')
    
    # Test logging a simple message
    message = "Test log message"
    log_entry = log_with_timestamp(message, log_file)
    
    # Check the log file contents
    with open(log_file, 'r') as f:
        contents = f.read()
    
    # Verify timestamp format and message
    assert contents.startswith('[')
    assert '] Test log message' in contents
    
    # Verify the return value
    assert message in log_entry

def test_log_creates_directory(tmp_path):
    # Test logging creates directory if it doesn't exist
    log_file = str(tmp_path / 'new_dir' / 'test.log')
    
    # Log a message
    log_with_timestamp("Directory creation test", log_file)
    
    # Check if file was created
    assert os.path.exists(log_file)

def test_multiple_logs(tmp_path):
    # Test multiple log entries
    log_file = str(tmp_path / 'multiple.log')
    
    # Log multiple messages
    log_with_timestamp("First message", log_file)
    log_with_timestamp("Second message", log_file)
    
    # Read log file
    with open(log_file, 'r') as f:
        contents = f.readlines()
    
    # Verify multiple entries
    assert len(contents) == 2
    assert 'First message' in contents[0]
    assert 'Second message' in contents[1]