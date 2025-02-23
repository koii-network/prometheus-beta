import pytest
from src.substring_extractor import extract_all_substrings

def test_extract_all_substrings_basic():
    """Test substring extraction for a simple string."""
    result = extract_all_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_extract_all_substrings_empty():
    """Test substring extraction for an empty string."""
    result = extract_all_substrings("")
    assert result == []

def test_extract_all_substrings_single_char():
    """Test substring extraction for a single character."""
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

def test_extract_all_substrings_repeated_chars():
    """Test substring extraction with repeated characters."""
    result = extract_all_substrings("aaa")
    expected = ['a', 'aa', 'aaa', 'a', 'aa', 'a']
    assert sorted(result) == sorted(expected)

def test_extract_all_substrings_special_chars():
    """Test substring extraction with special characters."""
    result = extract_all_substrings("a!b@c#")
    expected = ['a', 'a!', 'a!b', 'a!b@', 'a!b@c', 'a!b@c#', 
                '!', '!b', '!b@', '!b@c', '!b@c#',
                'b', 'b@', 'b@c', 'b@c#', 
                '@', '@c', '@c#', 
                'c', 'c#', 
                '#']
    assert sorted(result) == sorted(expected)