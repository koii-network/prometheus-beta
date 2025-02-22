import pytest
from src.char_frequency import get_char_frequency

def test_basic_char_frequency():
    """Test basic character frequency counting"""
    result = get_char_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    """Test character frequency for an empty string"""
    result = get_char_frequency("")
    assert result == {}

def test_mixed_characters():
    """Test character frequency with mixed characters and spaces"""
    result = get_char_frequency("Hello, World!")
    assert result == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}

def test_invalid_input():
    """Test that a TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_char_frequency(123)
        get_char_frequency(None)
        get_char_frequency(["hello"])