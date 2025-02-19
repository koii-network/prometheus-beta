import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test basic scenarios
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    
    # Test empty string
    assert find_longest_substring("") == ""
    
    # Test case sensitivity
    assert find_longest_substring("AbcA") == "AbcA"
    assert find_longest_substring("aA") == "aA"
    
    # Test with special characters and spaces
    assert find_longest_substring("hello world") == "helo wrd"
    
    # Test with long string
    assert find_longest_substring("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    
    # Test with repeated characters at different positions
    assert find_longest_substring("dvdf") == "vdf"
    
    # Additional edge cases
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("au") == "au"