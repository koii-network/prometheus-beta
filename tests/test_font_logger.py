"""
Tests for the font logging functionality.
"""

import pytest
from src.font_logger import log_with_font_size, FontSizeError

def test_default_log():
    """Test default logging behavior."""
    result = log_with_font_size("Hello World")
    assert result.startswith('🔸 ')
    assert "Hello World" in result

def test_different_sizes():
    """Test different font sizes."""
    small_log = log_with_font_size("Small", size='small')
    medium_log = log_with_font_size("Medium", size='medium')
    large_log = log_with_font_size("Large", size='large')
    xlarge_log = log_with_font_size("XLarge", size='xlarge')

    assert small_log.startswith('🔹 ')
    assert medium_log.startswith('🔸 ')
    assert large_log.startswith('🔶 ')
    assert xlarge_log.startswith('🔷 ')

def test_styling():
    """Test bold and italic styling."""
    bold_msg = log_with_font_size("Bold", bold=True)
    italic_msg = log_with_font_size("Italic", italic=True)
    bold_italic_msg = log_with_font_size("Bold Italic", bold=True, italic=True)

    assert bold_msg == '🔸 **Bold**'
    assert italic_msg == '🔸 *Italic*'
    assert bold_italic_msg == '🔸 ***Bold Italic***'

def test_invalid_size():
    """Test that invalid font sizes raise an error."""
    with pytest.raises(FontSizeError):
        log_with_font_size("Invalid", size='huge')

def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        log_with_font_size(123)

def test_empty_string():
    """Test logging an empty string."""
    result = log_with_font_size("")
    assert result == '🔸 '