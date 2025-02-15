import pytest
from src.font_logger import log_with_font_size

def test_default_font_size():
    """Test default medium font size"""
    result = log_with_font_size("Hello")
    assert result == '<span style="font-size: 12px;">Hello</span>'

def test_different_font_sizes():
    """Test all supported font sizes"""
    assert log_with_font_size("Small", "small") == '<span style="font-size: 8px;">Small</span>'
    assert log_with_font_size("Medium", "medium") == '<span style="font-size: 12px;">Medium</span>'
    assert log_with_font_size("Large", "large") == '<span style="font-size: 16px;">Large</span>'
    assert log_with_font_size("XLarge", "xlarge") == '<span style="font-size: 24px;">XLarge</span>'

def test_invalid_font_size():
    """Test that an invalid font size raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid font size"):
        log_with_font_size("Test", "huge")  # type: ignore

def test_empty_message():
    """Test logging an empty message"""
    result = log_with_font_size("")
    assert result == '<span style="font-size: 12px;"></span>'

def test_special_characters():
    """Test logging message with special characters"""
    result = log_with_font_size("Hello, World! @#$%")
    assert result == '<span style="font-size: 12px;">Hello, World! @#$%</span>'