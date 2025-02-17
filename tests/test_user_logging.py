import pytest
import logging
from src.user_logging import log_message, UserPermissionLevel

class TestUserLogging:
    def test_admin_can_log_all_levels(self, caplog):
        caplog.set_level(logging.DEBUG)
        
        # Test all log levels for admin
        assert log_message("Admin debug", UserPermissionLevel.ADMIN, 'debug') == True
        assert "[ADMIN] Admin debug" in caplog.text
        
        caplog.clear()
        assert log_message("Admin info", UserPermissionLevel.ADMIN, 'info') == True
        assert "[ADMIN] Admin info" in caplog.text
        
        caplog.clear()
        assert log_message("Admin warning", UserPermissionLevel.ADMIN, 'warning') == True
        assert "[ADMIN] Admin warning" in caplog.text
        
        caplog.clear()
        assert log_message("Admin error", UserPermissionLevel.ADMIN, 'error') == True
        assert "[ADMIN] Admin error" in caplog.text
    
    def test_user_logging_restrictions(self, caplog):
        caplog.set_level(logging.INFO)
        
        # User can log info and warning
        assert log_message("User info", UserPermissionLevel.USER, 'info') == True
        assert "[USER] User info" in caplog.text
        
        caplog.clear()
        assert log_message("User warning", UserPermissionLevel.USER, 'warning') == True
        assert "[USER] User warning" in caplog.text
        
        # User cannot log error or debug
        assert log_message("User error", UserPermissionLevel.USER, 'error') == False
        assert log_message("User debug", UserPermissionLevel.USER, 'debug') == False
    
    def test_guest_logging_restrictions(self, caplog):
        caplog.set_level(logging.INFO)
        
        # Guest can only log info
        assert log_message("Guest info", UserPermissionLevel.GUEST, 'info') == True
        assert "[GUEST] Guest info" in caplog.text
        
        # Guest cannot log other levels
        assert log_message("Guest warning", UserPermissionLevel.GUEST, 'warning') == False
        assert log_message("Guest error", UserPermissionLevel.GUEST, 'error') == False
    
    def test_invalid_inputs(self):
        # Test invalid message type
        with pytest.raises(TypeError):
            log_message(123, UserPermissionLevel.ADMIN)
        
        # Test invalid permission type
        with pytest.raises(TypeError):
            log_message("Test", "ADMIN")
        
        # Test invalid log level
        with pytest.raises(ValueError):
            log_message("Test", UserPermissionLevel.ADMIN, 'invalid_level')