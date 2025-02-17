import pytest
from src.character_frequency import find_most_frequent_character

def test_basic_string():
    """Test a simple string with a clear most frequent character."""
    assert find_most_frequent_character("hello") == "l"

def test_multiple_most_frequent():
    """Test a string where multiple characters have the same highest frequency."""
    result = find_most_frequent_character("aabbccdd")
    assert result in ['a', 'b', 'c', 'd']

def test_single_character():
    """Test a string with a single character."""
    assert find_most_frequent_character("x") == "x"

def test_mixed_case_string():
    """Test a string with mixed case characters."""
    assert find_most_frequent_character("AaaBbbCcc") == "a"

def test_special_characters():
    """Test a string with special characters."""
    assert find_most_frequent_character("!!@@##") == "!"

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError):
        find_most_frequent_character("")

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        find_most_frequent_character(123)
    with pytest.raises(TypeError):
        find_most_frequent_character(["a", "b", "c"])