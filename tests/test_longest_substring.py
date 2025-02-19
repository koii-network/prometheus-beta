import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test various scenarios
    assert find_longest_substring("") == ""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    assert find_longest_substring("abcdefg") == "abcdefg"
    
    # Case sensitivity tests
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"
    
    # Edge cases
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("dvdf") == "vdf"
    
    # Complex case with repeated characters at different positions
    assert find_longest_substring("tmmzuxt") == "mzuxt"