import os
import json
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.timestamp_logger import log_with_timestamp

def test_log_with_timestamp_dict(tmp_path):
    # Test logging a dictionary
    log_file = tmp_path / 'test_dict.log'
    test_dict = {'key': 'value', 'number': 42}
    
    result = log_with_timestamp(test_dict, str(log_file))
    
    # Verify result
    assert 'timestamp' in result
    assert 'data' in result
    assert result['data'] == test_dict
    
    # Verify file contents
    with open(log_file, 'r') as f:
        logged_line = json.loads(f.read().strip())
        assert logged_line['data'] == test_dict
        assert 'timestamp' in logged_line

def test_log_with_timestamp_string(tmp_path):
    # Test logging a string message
    log_file = tmp_path / 'test_string.log'
    test_message = "Test log message"
    
    result = log_with_timestamp(test_message, str(log_file))
    
    # Verify result
    assert 'timestamp' in result
    assert 'message' in result
    assert result['message'] == test_message
    
    # Verify file contents
    with open(log_file, 'r') as f:
        logged_line = json.loads(f.read().strip())
        assert logged_line['message'] == test_message
        assert 'timestamp' in logged_line

def test_log_with_timestamp_invalid_type():
    # Test logging an invalid type
    with pytest.raises(TypeError):
        log_with_timestamp(123)

def test_log_multiple_entries(tmp_path):
    # Test logging multiple entries to the same file
    log_file = tmp_path / 'multiple_entries.log'
    
    log_with_timestamp("First message", str(log_file))
    log_with_timestamp({"key": "value"}, str(log_file))
    
    # Verify file contents
    with open(log_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 2
        
        first_entry = json.loads(lines[0].strip())
        second_entry = json.loads(lines[1].strip())
        
        assert 'message' in first_entry
        assert 'data' in second_entry