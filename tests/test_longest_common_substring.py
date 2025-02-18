import pytest
from src.longest_common_substring import find_longest_common_substring

def test_find_longest_common_substring():
    # Basic cases
    assert find_longest_common_substring("hello", "help") == "hel"
    assert find_longest_common_substring("programming", "programmer") == "program"
    
    # Edge cases
    assert find_longest_common_substring("", "test") == ""
    assert find_longest_common_substring("test", "") == ""
    assert find_longest_common_substring("", "") == ""
    
    # No common substring
    assert find_longest_common_substring("xyz", "abc") == ""
    
    # Case sensitivity
    assert find_longest_common_substring("Hello", "hello") == ""
    
    # Multiple possible substrings
    assert find_longest_common_substring("abcdef", "bcdefa") == "bcde"
    
    # Repeated characters
    assert find_longest_common_substring("aaaaaa", "aaabaa") == "aaaa"
    
    # Partial match
    assert find_longest_common_substring("abcdefg", "cdefhij") == "cdef"

def test_substring_properties():
    # Test that the result is a continuous substring
    result = find_longest_common_substring("abcdefgh", "bcdxefgh")
    assert result == "bcdefgh" or result == "cdefgh"
    
    # Length of result should not exceed input strings
    s1, s2 = "hello world", "world hello"
    result = find_longest_common_substring(s1, s2)
    assert len(result) <= min(len(s1), len(s2))