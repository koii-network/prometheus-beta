import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_successful():
    session_data = {
        'user_id': 'test_user',
        'start_time': '2023-01-01 10:00:00',
        'actions': ['login', 'view_profile']
    }
    
    log_path = log_session_state(session_data)
    
    # Check if log file was created
    assert os.path.exists(log_path)
    
    # Verify log file contents
    with open(log_path, 'r') as log_file:
        logged_data = json.load(log_file)
    
    assert logged_data['user_id'] == 'test_user'
    assert 'log_timestamp' in logged_data

def test_log_session_state_custom_log_dir(tmp_path):
    session_data = {'key': 'value'}
    log_dir = tmp_path / 'custom_logs'
    
    log_path = log_session_state(session_data, log_dir=str(log_dir))
    
    assert os.path.exists(log_path)
    assert log_path.startswith(str(log_dir))

def test_log_session_state_invalid_input():
    # Test with non-dictionary input
    with pytest.raises(TypeError):
        log_session_state("not a dictionary")
    
    # Test with empty dictionary
    with pytest.raises(ValueError):
        log_session_state({})

def test_log_session_state_file_format():
    session_data = {'user': 'test'}
    log_path = log_session_state(session_data)
    
    # Check filename format
    assert log_path.startswith('logs/session_log_')
    assert log_path.endswith('.json')
    
    # Verify JSON file is valid and well-formatted
    with open(log_path, 'r') as log_file:
        logged_data = json.load(log_file)
    
    assert isinstance(logged_data, dict)