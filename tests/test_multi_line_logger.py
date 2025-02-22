import pytest
from src.multi_line_logger import log_multi_line

def test_basic_multi_line_logging():
    """Test basic multi-line logging functionality"""
    message = "Hello\nWorld"
    result = log_multi_line(message)
    
    # Check that result starts and ends with separator line
    lines = result.split('\n')
    assert lines[0].startswith('=')
    assert lines[-1].startswith('=')
    assert len(lines[0]) == 80  # default width
    assert len(lines) == 4  # separator + 2 lines + separator

def test_custom_separator():
    """Test logging with a custom separator"""
    message = "Custom\nSeparator"
    result = log_multi_line(message, separator='*', width=40)
    
    lines = result.split('\n')
    assert lines[0].startswith('*')
    assert lines[-1].startswith('*')
    assert len(lines[0]) == 40
    assert len(lines) == 4

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-string message
    with pytest.raises(TypeError):
        log_multi_line(123)
    
    # Test multi-character separator
    with pytest.raises(ValueError):
        log_multi_line("Test", separator='==')

def test_empty_message():
    """Test logging an empty message"""
    result = log_multi_line("")
    lines = result.split('\n')
    assert len(lines) == 3  # Just the two separator lines
    assert lines[0] == lines[-1]  # Separator lines are identical

def test_single_line_message():
    """Test logging a single-line message"""
    message = "Single line"
    result = log_multi_line(message)
    lines = result.split('\n')
    assert len(lines) == 3
    assert lines[1] == message