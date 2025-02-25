import pytest
from src.find_longest_substring import find_longest_substring

def test_find_longest_substring():
    # Basic cases
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    
    # Edge cases
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    
    # Complex cases
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"
    
    # Cases with multiple possible longest substrings
    assert find_longest_substring("abcdefg") == "abcdefg"
    
    # Mixed character cases
    assert find_longest_substring("aA1b2C3") == "aA1b2C3"
    
    # Repeated characters at different positions
    assert find_longest_substring("abcdeafghij") == "cdeafghij"

def test_find_longest_substring_error_handling():
    # Test with non-string input (should raise TypeError)
    with pytest.raises(TypeError):
        find_longest_substring(123)
    
    with pytest.raises(TypeError):
        find_longest_substring(None)