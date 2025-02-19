import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test various scenarios
    assert find_longest_substring("") == ""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    assert find_longest_substring("dvdf") == "vdf"
    
    # Test case with all unique characters
    assert find_longest_substring("abcdef") == "abcdef"
    
    # Test case with repeated characters at different positions
    assert find_longest_substring("asjrgapa") == "sjrgap"