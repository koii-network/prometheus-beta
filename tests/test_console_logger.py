import pytest
from src.console_logger import ConsoleLogger, UserPermissionLevel

def test_guest_logger_basic_logging(capsys):
    """Test that guest can log basic messages."""
    logger = ConsoleLogger(UserPermissionLevel.GUEST)
    result = logger.log("Guest message")
    captured = capsys.readouterr()
    assert result == "Guest message"
    assert "Guest message" in captured.out

def test_guest_logger_debug_logging(capsys):
    """Test that guest cannot log debug messages."""
    logger = ConsoleLogger(UserPermissionLevel.GUEST)
    result = logger.debug("Debug message")
    captured = capsys.readouterr()
    assert result is None
    assert "Debug message" not in captured.out

def test_user_logger_debug_logging(capsys):
    """Test that user can log debug messages."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    result = logger.debug("Debug message")
    captured = capsys.readouterr()
    assert result == "DEBUG: Debug message"
    assert "DEBUG: Debug message" in captured.out

def test_user_logger_error_logging(capsys):
    """Test that user cannot log error messages."""
    logger = ConsoleLogger(UserPermissionLevel.USER)
    result = logger.error("Error message")
    captured = capsys.readouterr()
    assert result is None
    assert "Error message" not in captured.out

def test_admin_logger_all_logging(capsys):
    """Test that admin can log all types of messages."""
    logger = ConsoleLogger(UserPermissionLevel.ADMIN)
    
    # Basic log
    basic_result = logger.log("Basic message")
    # Debug log
    debug_result = logger.debug("Debug message")
    # Error log
    error_result = logger.error("Error message")
    
    captured = capsys.readouterr()
    
    assert basic_result == "Basic message"
    assert debug_result == "DEBUG: Debug message"
    assert error_result == "ERROR: Error message"
    
    output = captured.out
    assert "Basic message" in output
    assert "DEBUG: Debug message" in output
    assert "ERROR: Error message" in output

def test_permission_levels():
    """Test the numeric values of permission levels."""
    assert UserPermissionLevel.GUEST.value == 0
    assert UserPermissionLevel.USER.value == 1
    assert UserPermissionLevel.ADMIN.value == 2
    assert UserPermissionLevel.GUEST.value < UserPermissionLevel.USER.value
    assert UserPermissionLevel.USER.value < UserPermissionLevel.ADMIN.value