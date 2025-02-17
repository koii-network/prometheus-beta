import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_basic():
    """Test basic logging functionality"""
    session_data = {
        'user': 'testuser',
        'actions': ['login', 'view_profile']
    }
    
    log_path = log_session_state(session_data)
    
    # Check file was created
    assert os.path.exists(log_path)
    
    # Verify file contents
    with open(log_path, 'r') as f:
        logged_data = json.load(f)
    
    assert logged_data['user'] == 'testuser'
    assert logged_data['actions'] == ['login', 'view_profile']
    assert 'logged_at' in logged_data

def test_log_session_state_custom_dir(tmp_path):
    """Test logging with a custom log directory"""
    session_data = {'test': 'custom_dir'}
    
    log_path = log_session_state(session_data, log_dir=str(tmp_path))
    
    assert os.path.exists(log_path)
    assert log_path.startswith(str(tmp_path))

def test_log_session_state_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(ValueError):
        log_session_state("not a dictionary")

def test_log_session_state_file_format():
    """Test that log file is a valid JSON with correct format"""
    session_data = {'key': 'value'}
    
    log_path = log_session_state(session_data)
    
    with open(log_path, 'r') as f:
        logged_data = json.load(f)
    
    assert isinstance(logged_data, dict)
    assert 'logged_at' in logged_data
    assert logged_data['key'] == 'value'