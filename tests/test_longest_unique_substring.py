import pytest
from src.longest_unique_substring import longest_unique_substring_length

def test_longest_unique_substring_length():
    # Basic test cases
    assert longest_unique_substring_length("abcabcbb") == 3
    assert longest_unique_substring_length("bbbbb") == 1
    assert longest_unique_substring_length("pwwkew") == 3
    
    # Edge cases
    assert longest_unique_substring_length("") == 0
    assert longest_unique_substring_length("a") == 1
    
    # More complex cases
    assert longest_unique_substring_length("dvdf") == 3
    assert longest_unique_substring_length("tmmzuxt") == 5
    
    # Case with repeated characters not next to each other
    assert longest_unique_substring_length("abcdefabcdef") == 6
    
    # Case with all unique characters
    assert longest_unique_substring_length("abcdefg") == 7