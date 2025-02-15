import os
import json
import pytest
from src.session_logger import log_session_state

def test_log_session_state_basic():
    # Test basic logging functionality
    session_data = {
        "user": "testuser",
        "action": "login",
        "status": "success"
    }
    
    log_file_path = log_session_state(session_data)
    
    # Check if file was created
    assert os.path.exists(log_file_path)
    
    # Verify file contents
    with open(log_file_path, 'r') as f:
        logged_data = json.load(f)
    
    assert "timestamp" in logged_data
    assert "session_details" in logged_data
    assert logged_data["session_details"] == session_data
    assert "environment" in logged_data

def test_log_session_state_custom_dir(tmp_path):
    # Test logging with a custom directory
    session_data = {"action": "test"}
    log_dir = tmp_path / "custom_logs"
    
    log_file_path = log_session_state(session_data, str(log_dir))
    
    assert os.path.exists(log_file_path)
    assert log_dir.as_posix() in log_file_path

def test_log_session_state_invalid_input():
    # Test invalid input raises ValueError
    with pytest.raises(ValueError):
        log_session_state("not a dictionary")

def test_log_session_state_unique_filenames():
    # Ensure multiple calls create unique filenames
    session_data = {"action": "test"}
    
    log_file_path1 = log_session_state(session_data)
    log_file_path2 = log_session_state(session_data)
    
    assert log_file_path1 != log_file_path2