import pytest
from src.multi_line_logger import log_multiline

def test_basic_multiline_logging():
    """Test basic multi-line logging functionality"""
    message = "Hello, World!"
    result = log_multiline(message)
    
    # Check the number of lines
    lines = result.split('\n')
    assert len(lines) == 3
    
    # Check separator lines
    assert lines[0] == '=' * 40
    assert lines[2] == '=' * 40
    
    # Check message
    assert lines[1] == message

def test_custom_separator():
    """Test logging with a custom separator"""
    message = "Custom Separator Test"
    result = log_multiline(message, separator='*', line_length=30)
    
    lines = result.split('\n')
    assert lines[0] == '*' * 30
    assert lines[2] == '*' * 30
    assert lines[1] == message

def test_invalid_message_type():
    """Test that non-string messages raise a TypeError"""
    with pytest.raises(TypeError):
        log_multiline(123)

def test_invalid_separator():
    """Test that multi-character separators raise a ValueError"""
    with pytest.raises(ValueError):
        log_multiline("Test", separator='==')

def test_invalid_line_length():
    """Test that negative or zero line lengths raise a ValueError"""
    with pytest.raises(ValueError):
        log_multiline("Test", line_length=0)
    
    with pytest.raises(ValueError):
        log_multiline("Test", line_length=-5)