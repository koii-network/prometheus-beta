import os
import json
import pytest
from src.timestamp_logger import log_with_timestamp
import datetime

def test_log_with_timestamp_basic():
    """Test basic logging functionality"""
    log_file = 'logs/test_basic_log.json'
    
    # Remove log file if it exists
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Log some test data
    log_with_timestamp("Test message", log_file=log_file)
    
    # Verify log file was created
    assert os.path.exists(log_file)
    
    # Read and verify log contents
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    log_entry = logs[0]
    
    assert 'timestamp' in log_entry
    assert 'level' in log_entry
    assert log_entry['data'] == "Test message"
    assert log_entry['level'] == 'INFO'
    
    # Verify timestamp is valid
    try:
        datetime.datetime.fromisoformat(log_entry['timestamp'])
    except ValueError:
        pytest.fail("Invalid timestamp format")

def test_log_with_different_levels():
    """Test logging with different log levels"""
    log_file = 'logs/test_levels_log.json'
    
    # Remove log file if it exists
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Log with different levels
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    for level in levels:
        log_with_timestamp(f"Test {level} message", log_file=log_file, log_level=level)
    
    # Read and verify log contents
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 5
    for log_entry, level in zip(logs, levels):
        assert log_entry['level'] == level

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_timestamp("Test message", log_level="INVALID")

def test_log_multiple_data_types():
    """Test logging different types of data"""
    log_file = 'logs/test_data_types_log.json'
    
    # Remove log file if it exists
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Log various data types
    test_data = [
        "String message",
        42,
        3.14,
        {"key": "value"},
        [1, 2, 3],
        None
    ]
    
    for data in test_data:
        log_with_timestamp(data, log_file=log_file)
    
    # Read and verify log contents
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == len(test_data)
    for log_entry, expected_data in zip(logs, test_data):
        assert log_entry['data'] == expected_data