import pytest
from src.unique_substrings import get_unique_substrings

def test_get_unique_substrings_basic():
    """Test unique substrings for a basic string."""
    result = get_unique_substrings("abc")
    assert set(result) == {'a', 'ab', 'abc', 'b', 'bc', 'c'}
    assert len(result) == 6

def test_get_unique_substrings_empty():
    """Test unique substrings for an empty string."""
    result = get_unique_substrings("")
    assert result == []

def test_get_unique_substrings_single_char():
    """Test unique substrings for a single character."""
    result = get_unique_substrings("x")
    assert result == ['x']

def test_get_unique_substrings_repeated_chars():
    """Test unique substrings with repeated characters."""
    result = get_unique_substrings("aaa")
    assert set(result) == {'a', 'aa', 'aaa'}
    assert len(result) == 3

def test_get_unique_substrings_mixed_chars():
    """Test unique substrings with mixed characters."""
    result = get_unique_substrings("hello")
    expected = {'h', 'he', 'hel', 'hell', 'hello', 
                'e', 'el', 'ell', 'ello', 
                'l', 'll', 'llo', 
                'l', 'lo', 
                'o'}
    assert set(result) == expected
    assert len(result) == 15