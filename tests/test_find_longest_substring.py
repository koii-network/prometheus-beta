import pytest
from src.find_longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test various scenarios
    assert find_longest_substring("") == ""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    assert find_longest_substring("dvdf") == "vdf"
    
def test_edge_cases():
    # Single character
    assert find_longest_substring("a") == "a"
    
    # All unique characters
    assert find_longest_substring("abcdef") == "abcdef"
    
    # Repeated unique substrings
    assert find_longest_substring("abcdeabcde") == "abcde"
    
def test_complex_cases():
    # Mixed case and special characters
    assert find_longest_substring("AbcABC") == "AbcABC"
    
    # Substring with spaces
    assert find_longest_substring("ab cd ef") == "ab cdef"