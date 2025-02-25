import pytest
from src.char_frequency import count_character_frequency

def test_basic_frequency():
    """Test basic character frequency counting."""
    result = count_character_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    """Test frequency of an empty string."""
    result = count_character_frequency("")
    assert result == {}

def test_string_with_spaces():
    """Test frequency counting with spaces."""
    result = count_character_frequency("hello world")
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_case_sensitivity():
    """Test that character counting is case-sensitive."""
    result = count_character_frequency("Hello")
    assert result == {'H': 1, 'e': 1, 'l': 2, 'o': 1}

def test_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_character_frequency(123)

def test_special_characters():
    """Test frequency counting with special characters."""
    result = count_character_frequency("a!b@c#")
    assert result == {'a': 1, '!': 1, 'b': 1, '@': 1, 'c': 1, '#': 1}