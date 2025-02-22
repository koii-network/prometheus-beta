import pytest
import colorama
from src.custom_logger import log_with_style

def test_log_with_style_default():
    """Test default logging without style"""
    message = "This is a test message"
    result = log_with_style(message)
    assert message in result
    assert colorama.Fore.RESET in result

def test_log_with_style_color():
    """Test logging with different color styles"""
    message = "Success message"
    
    # Test success style
    success_result = log_with_style(message, style='success')
    assert colorama.Fore.GREEN in success_result
    assert message in success_result

    # Test warning style
    warning_result = log_with_style(message, style='warning')
    assert colorama.Fore.YELLOW in warning_result
    assert message in warning_result

def test_log_with_style_indent():
    """Test message indentation"""
    message = "Indented message"
    result = log_with_style(message, indent=4)
    assert result.startswith('    ')
    assert message in result

def test_log_with_style_width():
    """Test message wrapping"""
    long_message = "This is a very long message that should be wrapped to a specific width for better readability"
    result = log_with_style(long_message, width=30)
    
    # Check if the message is wrapped
    lines = result.split('\n')
    assert len(lines) > 1
    assert all(len(line) <= 30 for line in lines)

def test_log_with_style_invalid_style():
    """Test handling of invalid style"""
    message = "Test message with invalid style"
    result = log_with_style(message, style='invalid')
    assert message in result
    assert colorama.Fore.RESET in result