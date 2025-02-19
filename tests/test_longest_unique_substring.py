import pytest
from src.longest_unique_substring import longest_unique_substring

def test_longest_unique_substring():
    # Test cases from the docstring
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    
    # Additional test cases
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("a") == 1
    assert longest_unique_substring("abcdef") == 6
    assert longest_unique_substring("dvdf") == 3
    
    # Repeated substring cases
    assert longest_unique_substring("aab") == 2
    assert longest_unique_substring("abba") == 2
    
    # Complex scenarios
    assert longest_unique_substring("tmmzuxt") == 5
    assert longest_unique_substring("abcdefghijklmnopqrstuvwxyz") == 26