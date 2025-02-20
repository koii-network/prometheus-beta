import pytest
from src.unique_chars import get_unique_sorted_chars

def test_get_unique_sorted_chars_basic():
    """Test basic functionality with a simple string"""
    assert get_unique_sorted_chars("hello") == ['e', 'h', 'l', 'o']

def test_get_unique_sorted_chars_case_sensitive():
    """Test case-sensitive sorting"""
    assert get_unique_sorted_chars("Python") == ['P', 'h', 'n', 'o', 't', 'y']

def test_get_unique_sorted_chars_empty_string():
    """Test with an empty string"""
    assert get_unique_sorted_chars("") == []

def test_get_unique_sorted_chars_repeated_chars():
    """Test with repeated characters"""
    assert get_unique_sorted_chars("aabbccAA") == ['A', 'a', 'b', 'c']

def test_get_unique_sorted_chars_special_chars():
    """Test with special characters and spaces"""
    assert get_unique_sorted_chars("Hello, World!") == [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r']

def test_get_unique_sorted_chars_invalid_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_unique_sorted_chars(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        get_unique_sorted_chars(None)