import pytest
from src.custom_logger import CustomLogger
import colorama

def test_custom_logger_initialization():
    """Test that the CustomLogger can be initialized."""
    logger = CustomLogger()
    assert isinstance(logger, CustomLogger)

def test_log_default_info():
    """Test logging with default info level."""
    logger = CustomLogger()
    message = "Test info message"
    result = logger.log(message)
    assert f"[INFO] {message}" in result
    assert colorama.Fore.BLUE in result

def test_log_warning():
    """Test logging with warning level."""
    logger = CustomLogger()
    message = "Test warning message"
    result = logger.log(message, level="warning")
    assert f"[WARNING] {message}" in result
    assert colorama.Fore.YELLOW in result

def test_log_error():
    """Test logging with error level."""
    logger = CustomLogger()
    message = "Test error message"
    result = logger.log(message, level="error")
    assert f"[ERROR] {message}" in result
    assert colorama.Fore.RED in result

def test_log_success():
    """Test logging with success level."""
    logger = CustomLogger()
    message = "Test success message"
    result = logger.log(message, level="success")
    assert f"[SUCCESS] {message}" in result
    assert colorama.Fore.GREEN in result

def test_log_custom_prefix():
    """Test logging with a custom prefix."""
    logger = CustomLogger()
    message = "Test message with custom prefix"
    result = logger.log(message, prefix="CUSTOM")
    assert "[CUSTOM] {message}" in result

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError."""
    logger = CustomLogger()
    with pytest.raises(ValueError, match="Invalid log level"):
        logger.log("Test message", level="invalid")  # type: ignore