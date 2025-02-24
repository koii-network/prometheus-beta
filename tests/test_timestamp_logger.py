import os
import json
import pytest
from datetime import datetime

# Import the function to test
from src.timestamp_logger import log_data

def test_log_data_basic(tmp_path):
    """Test basic logging functionality"""
    log_file = str(tmp_path / 'test_log.json')
    
    # Log some sample data
    log_data('test message', log_file)
    
    # Verify the log file was created and has correct content
    assert os.path.exists(log_file)
    
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    assert 'timestamp' in logs[0]
    assert 'data' in logs[0]
    assert logs[0]['data'] == 'test message'

def test_log_data_multiple_entries(tmp_path):
    """Test logging multiple entries to the same file"""
    log_file = str(tmp_path / 'multi_log.json')
    
    # Log multiple entries
    log_data('first message', log_file)
    log_data('second message', log_file)
    
    # Verify both entries are logged
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['data'] == 'first message'
    assert logs[1]['data'] == 'second message'

def test_log_data_different_types(tmp_path):
    """Test logging different types of data"""
    log_file = str(tmp_path / 'types_log.json')
    
    # Log various data types
    test_cases = [
        42,
        3.14,
        True,
        ['list', 'of', 'items'],
        {'key': 'value'},
        None
    ]
    
    for item in test_cases:
        log_data(item, log_file)
    
    # Verify all entries are logged
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == len(test_cases)
    for i, item in enumerate(test_cases):
        assert logs[i]['data'] == item

def test_log_data_timestamp_format(tmp_path):
    """Test that timestamp is in correct ISO format"""
    log_file = str(tmp_path / 'timestamp_log.json')
    
    log_data('timestamp test', log_file)
    
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    # Try parsing the timestamp to verify it's in ISO format
    try:
        datetime.fromisoformat(logs[0]['timestamp'])
    except ValueError:
        pytest.fail("Timestamp is not in valid ISO format")

def test_log_data_directory_creation(tmp_path):
    """Test that directories are created if they don't exist"""
    log_file = str(tmp_path / 'deep' / 'nested' / 'log.json')
    
    log_data('directory test', log_file)
    
    assert os.path.exists(log_file)

def test_log_data_existing_file(tmp_path):
    """Test appending to an existing log file"""
    log_file = str(tmp_path / 'append_log.json')
    
    # Create initial log
    with open(log_file, 'w') as f:
        json.dump([{'timestamp': '2023-01-01T00:00:00', 'data': 'initial'}], f)
    
    # Append new log
    log_data('new message', log_file)
    
    # Verify both entries exist
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[1]['data'] == 'new message'