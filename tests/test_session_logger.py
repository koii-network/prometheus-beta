import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_basic():
    # Test basic functionality
    session_data = {
        'user': 'testuser',
        'session_id': '12345',
        'status': 'active'
    }
    
    log_path = log_session_state(session_data)
    
    # Check file was created
    assert os.path.exists(log_path)
    
    # Verify file contents
    with open(log_path, 'r') as f:
        logged_data = json.load(f)
    
    assert logged_data['user'] == 'testuser'
    assert logged_data['session_id'] == '12345'
    assert logged_data['status'] == 'active'
    assert 'timestamp' in logged_data

def test_log_session_state_custom_dir(tmp_path):
    # Test logging to a custom directory
    session_data = {
        'user': 'customuser',
        'session_id': '67890'
    }
    
    custom_log_dir = tmp_path / 'custom_logs'
    log_path = log_session_state(session_data, log_dir=str(custom_log_dir))
    
    assert os.path.exists(log_path)
    assert str(custom_log_dir) in log_path

def test_log_session_state_invalid_input():
    # Test invalid input raises ValueError
    with pytest.raises(ValueError):
        log_session_state("Not a dictionary")
    
    with pytest.raises(ValueError):
        log_session_state(None)

def test_log_session_state_file_creation():
    # Test that multiple calls create unique files
    session_data = {'test': 'data'}
    
    log_path1 = log_session_state(session_data)
    log_path2 = log_session_state(session_data)
    
    assert log_path1 != log_path2  # Different timestamps should create different files