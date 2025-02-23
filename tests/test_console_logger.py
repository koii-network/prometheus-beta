import pytest
from src.console_logger import ConsoleLogger, UserPermissionLevel

def test_logger_guest_permissions():
    """Test logging behavior for a guest user."""
    logger = ConsoleLogger(UserPermissionLevel.GUEST)
    
    # Guest should only log messages at GUEST level
    assert logger.log("Guest message") is None
    assert logger.log("User message", UserPermissionLevel.USER) is None
    assert logger.log_error("Error message") is None
    assert logger.log_debug("Debug message") is None

def test_logger_user_permissions():
    """Test logging behavior for a regular user."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    
    # User should log messages at USER and lower levels
    assert logger.log("Guest message") is not None
    assert logger.log("User message", UserPermissionLevel.USER) is not None
    assert logger.log_error("Error message") is None
    assert logger.log_debug("Debug message") is None

def test_logger_admin_permissions():
    """Test logging behavior for an admin user."""
    logger = ConsoleLogger(UserPermissionLevel.ADMIN)
    
    # Admin should log all levels of messages
    assert logger.log("Guest message") is not None
    assert logger.log("User message", UserPermissionLevel.USER) is not None
    assert logger.log_error("Error message") is not None
    assert logger.log_debug("Debug message") is not None

def test_log_method_default_permissions():
    """Test default permission levels for different log methods."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    
    # Default log requires USER permission
    assert logger.log("User message") is not None
    
    # Error and debug logs require ADMIN permission by default
    assert logger.log_error("Error message") is None
    assert logger.log_debug("Debug message") is None

def test_custom_minimum_permissions():
    """Test custom minimum permission levels."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    
    # Custom permission level that requires ADMIN
    assert logger.log("Admin-only message", UserPermissionLevel.ADMIN) is None
    
    # Custom permission level compatible with USER
    assert logger.log("User-specific message", UserPermissionLevel.USER) is not None