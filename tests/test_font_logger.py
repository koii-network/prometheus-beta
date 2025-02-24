import pytest
from src.font_logger import log_with_font_size

def test_default_font_size():
    """Test default medium font size"""
    result = log_with_font_size("Hello")
    assert result == "[MEDIUM] Hello"

def test_small_font_size():
    """Test small font size"""
    result = log_with_font_size("Hello", size='small')
    assert result == "[SMALL] Hello"

def test_large_font_size():
    """Test large font size"""
    result = log_with_font_size("Hello", size='large')
    assert result == "[LARGE] Hello"

def test_invalid_font_size():
    """Test that invalid font size raises ValueError"""
    with pytest.raises(ValueError, match="Invalid font size"):
        log_with_font_size("Hello", size='extra-large')  # type: ignore

def test_different_messages():
    """Test logging different messages with various sizes"""
    assert log_with_font_size("Test 1") == "[MEDIUM] Test 1"
    assert log_with_font_size("Test 2", 'small') == "[SMALL] Test 2"
    assert log_with_font_size("Test 3", 'large') == "[LARGE] Test 3"