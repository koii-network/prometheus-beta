import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test various scenarios
    assert find_longest_substring("") == ""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    
    # Case-sensitive tests
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"
    
    # Edge cases
    assert find_longest_substring("dvdf") == "vdf"
    
    # Long string with multiple candidates
    assert find_longest_substring("abcdefghijklmnopqrstuvwxyzABCDEFG") == "abcdefghijklmnopqrstuvwxyzABCDEFG"

def test_find_longest_substring_no_repeats():
    assert find_longest_substring("abcdefg") == "abcdefg"

def test_find_longest_substring_single_char():
    assert find_longest_substring("a") == "a"