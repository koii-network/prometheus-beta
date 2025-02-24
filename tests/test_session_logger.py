import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_basic():
    """Test basic logging functionality"""
    log_file = log_session_state()
    
    # Check file was created
    assert os.path.exists(log_file)
    
    # Verify file contents
    with open(log_file, 'r') as f:
        log_data = json.load(f)
    
    assert 'timestamp' in log_data
    assert 'caller_info' in log_data
    assert 'context' in log_data
    assert log_data['context'] == {}

def test_log_session_state_with_context():
    """Test logging with custom context"""
    test_context = {'user': 'test_user', 'session_id': '12345'}
    log_file = log_session_state(session_context=test_context)
    
    with open(log_file, 'r') as f:
        log_data = json.load(f)
    
    assert log_data['context'] == test_context

def test_log_session_state_custom_path(tmp_path):
    """Test logging with custom log path"""
    custom_log_path = str(tmp_path / 'custom_logs')
    log_file = log_session_state(log_path=custom_log_path)
    
    assert log_file.startswith(custom_log_path)
    assert os.path.exists(log_file)

def test_log_session_state_caller_info():
    """Test that caller information is correctly captured"""
    log_file = log_session_state()
    
    with open(log_file, 'r') as f:
        log_data = json.load(f)
    
    assert 'caller_info' in log_data
    assert 'filename' in log_data['caller_info']
    assert 'function_name' in log_data['caller_info']
    assert 'line_number' in log_data['caller_info']