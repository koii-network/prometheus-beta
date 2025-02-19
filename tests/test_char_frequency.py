import pytest
from src.char_frequency import get_char_frequency

def test_basic_character_frequency():
    """Test basic character frequency counting."""
    result = get_char_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    """Test frequency of an empty string."""
    result = get_char_frequency("")
    assert result == {}

def test_string_with_spaces():
    """Test character frequency with spaces."""
    result = get_char_frequency("hello world")
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_char_frequency(123)

def test_string_with_special_characters():
    """Test character frequency with special characters."""
    result = get_char_frequency("hello!@#")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1, '!': 1, '@': 1, '#': 1}