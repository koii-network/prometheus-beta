import pytest
from src.colored_logger import BackgroundColorLogger

def test_log_default():
    """Test logging without colors"""
    message = "Test message"
    result = BackgroundColorLogger.log(message)
    assert message in result

def test_log_with_background_color():
    """Test logging with a background color"""
    message = "Colored background message"
    result = BackgroundColorLogger.log(message, background_color='green')
    assert message in result
    assert '\033[42m' in result  # Green background color code
    assert '\033[0m' in result   # Reset code

def test_log_with_text_color():
    """Test logging with a text color"""
    message = "Colored text message"
    result = BackgroundColorLogger.log(message, text_color='red')
    assert message in result
    assert '\033[31m' in result  # Red text color code
    assert '\033[0m' in result   # Reset code

def test_log_with_background_and_text_colors():
    """Test logging with both background and text colors"""
    message = "Multicolor message"
    result = BackgroundColorLogger.log(message, background_color='blue', text_color='yellow')
    assert message in result
    assert '\033[44m' in result  # Blue background color code
    assert '\033[33m' in result  # Yellow text color code
    assert '\033[0m' in result   # Reset code

def test_invalid_background_color():
    """Test that an invalid background color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        BackgroundColorLogger.log("Test", background_color='invalid_color')

def test_invalid_text_color():
    """Test that an invalid text color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        BackgroundColorLogger.log("Test", text_color='invalid_color')