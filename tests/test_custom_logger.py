import pytest
import colorama
from src.custom_logger import log_message

def test_default_info_log(capsys):
    """Test default info log level"""
    result = log_message("Test info message")
    captured = capsys.readouterr()
    assert colorama.Fore.BLUE in result
    assert "[INFO] Test info message" in result

def test_warning_log(capsys):
    """Test warning log level"""
    result = log_message("Warning occurred", level='warning')
    captured = capsys.readouterr()
    assert colorama.Fore.YELLOW in result
    assert "[WARNING] Warning occurred" in result

def test_error_log(capsys):
    """Test error log level"""
    result = log_message("Error happened", level='error')
    captured = capsys.readouterr()
    assert colorama.Fore.RED in result
    assert "[ERROR] Error happened" in result

def test_success_log(capsys):
    """Test success log level"""
    result = log_message("Operation successful", level='success')
    captured = capsys.readouterr()
    assert colorama.Fore.GREEN in result
    assert "[SUCCESS] Operation successful" in result

def test_custom_prefix(capsys):
    """Test custom prefix functionality"""
    result = log_message("Custom prefix test", prefix="[CUSTOM] ")
    captured = capsys.readouterr()
    assert "[CUSTOM] Custom prefix test" in result

def test_invalid_log_level():
    """Test that invalid log level raises ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_message("Invalid message", level='invalid')  # type: ignore