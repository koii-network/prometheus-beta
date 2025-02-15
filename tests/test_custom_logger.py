import pytest
import colorama
from src.custom_logger import CustomLogger

def test_default_log():
    """Test logging a message without color or style"""
    result = CustomLogger.log("Test message")
    assert result == "Test message"

def test_log_with_color():
    """Test logging a message with a specific color"""
    result = CustomLogger.log("Colored message", color='green')
    assert result.startswith(colorama.Fore.GREEN + "Colored message")

def test_log_with_style():
    """Test logging a message with a specific style"""
    result = CustomLogger.log("Styled message", style='bright')
    assert result.startswith(colorama.Style.BRIGHT + "Styled message")

def test_log_with_color_and_style():
    """Test logging a message with both color and style"""
    result = CustomLogger.log("Colored and styled message", color='blue', style='dim')
    assert result.startswith(colorama.Fore.BLUE + colorama.Style.DIM + "Colored and styled message")

def test_log_with_prefix():
    """Test logging a message with a prefix"""
    result = CustomLogger.log("Message with prefix", prefix="[TEST]")
    assert result == "[TEST] Message with prefix"

def test_invalid_color():
    """Test that an invalid color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid color"):
        CustomLogger.log("Invalid color", color='invalid_color')

def test_invalid_style():
    """Test that an invalid style raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid style"):
        CustomLogger.log("Invalid style", style='invalid_style')