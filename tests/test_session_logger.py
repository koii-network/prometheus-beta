import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_basic():
    # Test basic logging functionality
    session_data = {
        'user': 'testuser',
        'actions': ['login', 'view_profile']
    }
    
    log_path = log_session_state(session_data)
    
    # Check if log file exists
    assert os.path.exists(log_path)
    
    # Verify log file content
    with open(log_path, 'r') as log_file:
        logged_data = json.load(log_file)
    
    assert logged_data['user'] == 'testuser'
    assert logged_data['actions'] == ['login', 'view_profile']
    assert 'log_timestamp' in logged_data

def test_log_session_state_custom_dir(tmpdir):
    # Test logging with a custom directory
    session_data = {
        'user': 'customuser',
        'actions': ['signup']
    }
    
    log_path = log_session_state(session_data, log_dir=str(tmpdir))
    
    # Check if log file exists in the specified directory
    assert os.path.exists(log_path)
    assert str(tmpdir) in log_path

def test_log_session_state_invalid_input():
    # Test with invalid input types
    with pytest.raises(TypeError):
        log_session_state("not a dictionary")
    
    with pytest.raises(ValueError):
        log_session_state({})

def test_log_session_state_multiple_logs(tmpdir):
    # Test creating multiple log files
    session1 = {'user': 'user1', 'action': 'test1'}
    session2 = {'user': 'user2', 'action': 'test2'}
    
    log_path1 = log_session_state(session1, log_dir=str(tmpdir))
    log_path2 = log_session_state(session2, log_dir=str(tmpdir))
    
    # Ensure different log files are created
    assert log_path1 != log_path2