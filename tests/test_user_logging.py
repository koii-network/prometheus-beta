import pytest
import logging
from src.user_logging import log_message, UserPermissionLevel

def test_log_message_valid_inputs(caplog):
    caplog.set_level(logging.INFO)
    result = log_message("Test message", UserPermissionLevel.USER)
    assert result is True
    assert "Test message" in caplog.text

def test_guest_permission_restrictions(caplog):
    # Guests should not be able to log debug, error, or critical messages
    caplog.set_level(logging.DEBUG)
    
    # Debug should fail
    result = log_message("Debug message", UserPermissionLevel.GUEST, 'debug')
    assert result is False
    
    # Error should fail
    result = log_message("Error message", UserPermissionLevel.GUEST, 'error')
    assert result is False
    
    # Critical should fail
    result = log_message("Critical message", UserPermissionLevel.GUEST, 'critical')
    assert result is False

def test_user_permission_restrictions(caplog):
    # Users should not be able to log debug messages
    caplog.set_level(logging.DEBUG)
    
    result = log_message("Debug message", UserPermissionLevel.USER, 'debug')
    assert result is False

def test_admin_permission_full_access(caplog):
    caplog.set_level(logging.DEBUG)
    
    # Admin should be able to log all levels
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        result = log_message(f"{level.capitalize()} message", UserPermissionLevel.ADMIN, level)
        assert result is True

def test_invalid_inputs():
    # Test invalid message type
    with pytest.raises(TypeError):
        log_message(123, UserPermissionLevel.USER)
    
    # Test invalid permission
    with pytest.raises(TypeError):
        log_message("Test", "invalid_permission")
    
    # Test invalid log level
    with pytest.raises(ValueError):
        log_message("Test", UserPermissionLevel.USER, "invalid_level")