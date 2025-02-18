import pytest
from src.substring_extractor import extract_all_substrings

def test_extract_all_substrings_normal_case():
    """Test substring extraction for a typical string."""
    result = extract_all_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_extract_all_substrings_empty_string():
    """Test substring extraction for an empty string."""
    result = extract_all_substrings("")
    assert result == []

def test_extract_all_substrings_single_char():
    """Test substring extraction for a single character string."""
    result = extract_all_substrings("x")
    assert result == ['x']

def test_extract_all_substrings_longer_string():
    """Test substring extraction for a longer string."""
    result = extract_all_substrings("hello")
    expected = ['h', 'he', 'hel', 'hell', 'hello', 
                'e', 'el', 'ell', 'ello', 
                'l', 'll', 'llo', 
                'l', 'lo', 
                'o']
    assert sorted(result) == sorted(expected)

def test_extract_all_substrings_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_all_substrings(123)
        extract_all_substrings(None)