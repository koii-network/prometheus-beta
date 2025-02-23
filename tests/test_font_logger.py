"""
Test suite for font logging functionality.
"""

import pytest
from src.font_logger import log_with_font_size, FontSizeError

def test_default_log():
    """Test default logging without style."""
    result = log_with_font_size("Hello World")
    assert "[Font Size: 12]" in result
    assert "Hello World" in result

def test_custom_font_size():
    """Test logging with custom font size."""
    result = log_with_font_size("Hello World", size=24)
    assert "[Font Size: 24]" in result
    assert "Hello World" in result

def test_bold_style():
    """Test logging with bold style."""
    result = log_with_font_size("Hello World", style='bold')
    assert "[Font Size: 12]" in result
    assert "**Hello World**" in result

def test_italic_style():
    """Test logging with italic style."""
    result = log_with_font_size("Hello World", style='italic')
    assert "[Font Size: 12]" in result
    assert "*Hello World*" in result

def test_underline_style():
    """Test logging with underline style."""
    result = log_with_font_size("Hello World", style='underline')
    assert "[Font Size: 12]" in result
    assert "_Hello World_" in result

def test_invalid_size_low():
    """Test that size below 6 raises an error."""
    with pytest.raises(FontSizeError):
        log_with_font_size("Hello", size=5)

def test_invalid_size_high():
    """Test that size above 72 raises an error."""
    with pytest.raises(FontSizeError):
        log_with_font_size("Hello", size=73)

def test_invalid_size_type():
    """Test that non-integer size raises a TypeError."""
    with pytest.raises(TypeError):
        log_with_font_size("Hello", size="12")

def test_invalid_message_type():
    """Test that non-string message raises a TypeError."""
    with pytest.raises(TypeError):
        log_with_font_size(123)

def test_invalid_style():
    """Test that invalid style raises a ValueError."""
    with pytest.raises(ValueError):
        log_with_font_size("Hello", style="invalid")