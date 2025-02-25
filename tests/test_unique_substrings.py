import pytest
from src.unique_substrings import get_unique_substrings

def test_basic_substrings():
    """Test basic substring generation."""
    result = get_unique_substrings("abc")
    assert result == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_empty_string():
    """Test handling of empty string."""
    result = get_unique_substrings("")
    assert result == []

def test_single_character():
    """Test single character input."""
    result = get_unique_substrings("a")
    assert result == ['a']

def test_repeated_characters():
    """Test string with repeated characters."""
    result = get_unique_substrings("aaa")
    assert result == ['a', 'aa', 'aaa']

def test_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_unique_substrings(123)
        get_unique_substrings(None)

def test_complex_string():
    """Test with a more complex string."""
    result = get_unique_substrings("hello")
    expected = ['e', 'el', 'ell', 'ello', 'h', 'he', 'hel', 'hell', 'hello', 'l', 'll', 'llo', 'lo', 'o']
    assert result == expected