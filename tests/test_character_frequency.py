import pytest
from src.character_frequency import get_character_frequency

def test_basic_character_frequency():
    """Test basic character frequency counting"""
    result = get_character_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    """Test frequency of an empty string"""
    result = get_character_frequency("")
    assert result == {}

def test_repeated_characters():
    """Test string with multiple repeated characters"""
    result = get_character_frequency("aaaaabbbcc")
    assert result == {'a': 5, 'b': 3, 'c': 2}

def test_case_sensitivity():
    """Test that the function is case-sensitive"""
    result = get_character_frequency("HelLo")
    assert result == {'H': 1, 'e': 1, 'l': 2, 'L': 1, 'o': 1}

def test_with_special_characters():
    """Test string with special characters and spaces"""
    result = get_character_frequency("hello, world!")
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, ',': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

def test_invalid_input_type():
    """Test that the function raises TypeError for non-string inputs"""
    with pytest.raises(TypeError):
        get_character_frequency(12345)
    
    with pytest.raises(TypeError):
        get_character_frequency(None)