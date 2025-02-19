import pytest
from src.unique_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of finding the longest unique substring."""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases for the function."""
    assert find_longest_substring("") == ""  # Empty string
    assert find_longest_substring("a") == "a"  # Single character
    assert find_longest_substring("abcdefg") == "abcdefg"  # All unique characters

def test_find_longest_substring_multiple_candidates():
    """Test cases with multiple possible longest unique substrings."""
    assert find_longest_substring("abcdeapbcdef") == "abcde"
    assert find_longest_substring("dvdf") == "vdf"

def test_find_longest_substring_special_characters():
    """Test with strings containing special characters and spaces."""
    assert find_longest_substring("a b c d") == "a b c d"
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"