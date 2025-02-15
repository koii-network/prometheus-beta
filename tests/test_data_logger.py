import os
import json
import pytest
from src.data_logger import log_data

def test_log_data_success(tmp_path):
    """Test successful logging of data"""
    log_file = os.path.join(tmp_path, 'test_log.json')
    test_data = {'key': 'value', 'number': 42}
    
    result = log_data(test_data, log_file)
    assert result is True
    
    # Verify the log file was created and contains the correct data
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    assert 'timestamp' in logs[0]
    assert logs[0]['data'] == test_data

def test_log_data_multiple_entries(tmp_path):
    """Test logging multiple entries to the same file"""
    log_file = os.path.join(tmp_path, 'multi_log.json')
    test_data1 = {'key1': 'value1'}
    test_data2 = {'key2': 'value2'}
    
    log_data(test_data1, log_file)
    log_data(test_data2, log_file)
    
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['data'] == test_data1
    assert logs[1]['data'] == test_data2

def test_log_data_invalid_input(tmp_path):
    """Test logging with invalid input"""
    log_file = os.path.join(tmp_path, 'invalid_log.json')
    
    # Test with non-serializable data
    class CustomClass:
        pass
    
    result = log_data(CustomClass(), log_file)
    assert result is False