import pytest
import sys
from io import StringIO
from src.custom_logger import log_message, LogStyle

def test_log_message_default():
    """Test basic logging without any styling"""
    message = log_message("Test message")
    assert message == "Test message" + LogStyle.RESET

def test_log_message_with_color():
    """Test logging with different colors"""
    red_message = log_message("Error message", color=LogStyle.RED)
    assert red_message.startswith(LogStyle.RED)
    assert red_message.endswith(LogStyle.RESET)

def test_log_message_with_prefix():
    """Test logging with a prefix"""
    prefixed_message = log_message("Test", prefix="[INFO]")
    assert prefixed_message.startswith("[INFO] Test")

def test_log_message_bold():
    """Test logging with bold styling"""
    bold_message = log_message("Bold text", bold=True)
    assert bold_message.startswith("\033[1m")

def test_log_message_color_and_bold():
    """Test logging with both color and bold"""
    styled_message = log_message("Styled message", color=LogStyle.GREEN, bold=True)
    assert styled_message.startswith("\033[1m" + LogStyle.GREEN)

def test_log_message_invalid_color():
    """Test that an invalid color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid color"):
        log_message("Test", color="invalid_color")

def test_log_message_output(capsys):
    """Test that the message is printed to stdout"""
    log_message("Captured message")
    captured = capsys.readouterr()
    assert "Captured message" in captured.out