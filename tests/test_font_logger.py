import pytest
from src.font_logger import log_with_font_size

def test_default_medium_font_size():
    """Test default medium font size."""
    result = log_with_font_size("Hello World")
    assert result == "[Font:14px] Hello World"

def test_predefined_font_sizes():
    """Test predefined font sizes."""
    assert log_with_font_size("Small", 'small') == "[Font:10px] Small"
    assert log_with_font_size("Medium", 'medium') == "[Font:14px] Medium"
    assert log_with_font_size("Large", 'large') == "[Font:18px] Large"

def test_custom_pixel_size():
    """Test custom pixel size."""
    result = log_with_font_size("Custom", 20)
    assert result == "[Font:20px] Custom"

def test_invalid_predefined_size():
    """Test invalid predefined size raises ValueError."""
    with pytest.raises(ValueError, match="Invalid predefined font size"):
        log_with_font_size("Error", 'xlarge')

def test_invalid_font_size_type():
    """Test invalid font size type raises TypeError."""
    with pytest.raises(TypeError, match="Font size must be a string or integer"):
        log_with_font_size("Error", 3.14)

def test_negative_font_size():
    """Test negative font size raises ValueError."""
    with pytest.raises(ValueError, match="Font size must be a positive integer"):
        log_with_font_size("Error", -10)

def test_case_insensitive_predefined_sizes():
    """Test case insensitivity for predefined sizes."""
    assert log_with_font_size("Mixed", 'SMALL') == "[Font:10px] Mixed"
    assert log_with_font_size("Mixed", 'Large') == "[Font:18px] Large"