import os
import json
import pytest
from datetime import datetime
import sys
sys.path.append('src')

from timestamp_logger import log_data_with_timestamp

@pytest.fixture
def temp_log_file(tmp_path):
    """Create a temporary log file for testing"""
    return str(tmp_path / "test_log.json")

def test_log_data_with_timestamp_success(temp_log_file):
    """Test successful logging of data"""
    data = {"key": "value", "number": 42}
    result = log_data_with_timestamp(data, temp_log_file)
    
    # Check returned log entry
    assert 'timestamp' in result
    assert 'data' in result
    assert result['data'] == data
    
    # Verify file contents
    with open(temp_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    assert logs[0]['data'] == data
    assert datetime.fromisoformat(logs[0]['timestamp'])  # Check timestamp is valid

def test_log_data_with_timestamp_multiple_entries(temp_log_file):
    """Test logging multiple entries to the same file"""
    data1 = {"first": "entry"}
    data2 = {"second": "entry"}
    
    log_data_with_timestamp(data1, temp_log_file)
    log_data_with_timestamp(data2, temp_log_file)
    
    with open(temp_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['data'] == data1
    assert logs[1]['data'] == data2

def test_log_data_with_timestamp_invalid_input():
    """Test error handling for invalid inputs"""
    # Test non-dictionary input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_data_with_timestamp("not a dict")
    
    # Test empty dictionary
    with pytest.raises(ValueError, match="Data cannot be empty"):
        log_data_with_timestamp({})

def test_log_directory_creation(tmp_path):
    """Test that log directory is created if it doesn't exist"""
    log_dir = str(tmp_path / "logs")
    log_file = os.path.join(log_dir, "new_log.json")
    
    data = {"test": "directory creation"}
    log_data_with_timestamp(data, log_file)
    
    assert os.path.exists(log_file)
    
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    assert logs[0]['data'] == data