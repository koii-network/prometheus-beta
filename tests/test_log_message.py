import pytest
from src.log_message import log_message, LogStyle

def test_log_message_basic():
    """Test basic logging without styling"""
    result = log_message("Hello, World!")
    assert "Hello, World!" in result

def test_log_message_with_color():
    """Test logging with different colors"""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        result = log_message("Test", color=color)
        assert result is not None

def test_log_message_with_style():
    """Test logging with different styles"""
    styles = ['bright', 'dim', 'normal']
    for style in styles:
        result = log_message("Test", style=style)
        assert result is not None

def test_log_message_with_prefix():
    """Test logging with a prefix"""
    result = log_message("Test", prefix="INFO:")
    assert "INFO: Test" in result

def test_log_message_full_styling():
    """Test logging with full styling"""
    result = log_message("Test", color='green', style='bright', prefix='SUCCESS:')
    assert "SUCCESS: Test" in result

def test_invalid_color():
    """Test that invalid color raises ValueError"""
    with pytest.raises(ValueError):
        log_message("Test", color='invalid_color')

def test_invalid_style():
    """Test that invalid style raises ValueError"""
    with pytest.raises(ValueError):
        log_message("Test", style='invalid_style')

def test_empty_message():
    """Test logging an empty message"""
    result = log_message("")
    assert result == ""

def test_unicode_message():
    """Test logging a message with unicode characters"""
    result = log_message("こんにちは")
    assert "こんにちは" in result