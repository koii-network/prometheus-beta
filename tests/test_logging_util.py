import pytest
from src.logging_util import log_with_font_size

def test_default_font_size():
    """Test default font size of 2"""
    result = log_with_font_size("Hello")
    assert result == '<font size="2">Hello</font>'

def test_different_font_sizes():
    """Test different font sizes"""
    assert log_with_font_size("Small", 1) == '<font size="1">Small</font>'
    assert log_with_font_size("Medium", 2) == '<font size="2">Medium</font>'
    assert log_with_font_size("Large", 3) == '<font size="3">Large</font>'

def test_invalid_font_size():
    """Test invalid font size raises ValueError"""
    with pytest.raises(ValueError, match="Font size must be 1, 2, or 3"):
        log_with_font_size("Invalid", 4)
    
    with pytest.raises(ValueError, match="Font size must be 1, 2, or 3"):
        log_with_font_size("Invalid", 0)