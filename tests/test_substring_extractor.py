import pytest
from src.substring_extractor import extract_substrings

def test_extract_substrings_normal_string():
    """Test substring extraction for a normal string."""
    result = extract_substrings("abc")
    expected = ['', 'a', 'b', 'c', 'ab', 'bc', 'abc']
    assert sorted(result) == sorted(expected)

def test_extract_substrings_empty_string():
    """Test substring extraction for an empty string."""
    result = extract_substrings("")
    assert result == ['']

def test_extract_substrings_single_char():
    """Test substring extraction for a single character string."""
    result = extract_substrings("x")
    expected = ['', 'x']
    assert sorted(result) == sorted(expected)

def test_extract_substrings_longer_string():
    """Test substring extraction for a longer string."""
    result = extract_substrings("hello")
    expected = ['', 'h', 'e', 'l', 'l', 'o', 
                'he', 'el', 'll', 'lo', 
                'hel', 'ell', 'llo', 
                'hell', 'ello', 
                'hello']
    assert sorted(result) == sorted(expected)

def test_extract_substrings_with_repeated_chars():
    """Test substring extraction with repeated characters."""
    result = extract_substrings("aaa")
    expected = ['', 'a', 'a', 'a', 'aa', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)

def test_extract_substrings_special_chars():
    """Test substring extraction with special characters."""
    result = extract_substrings("a!b@c")
    expected = ['', 'a', '!', 'b', '@', 'c', 
                'a!', '!b', 'b@', '@c', 
                'a!b', '!b@', 'b@c', 
                'a!b@', '!b@c', 
                'a!b@c']
    assert sorted(result) == sorted(expected)