import pytest
from src.substring_finder import find_longest_substring

def test_normal_cases():
    """Test typical input scenarios"""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_edge_cases():
    """Test edge case scenarios"""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_unique_string():
    """Test strings where all characters are unique"""
    assert find_longest_substring("abcdef") == "abcdef"

def test_repeated_characters():
    """Test strings with multiple repeated characters"""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"

def test_unicode_characters():
    """Test function with unicode characters"""
    assert find_longest_substring("こんにちは") == "こんにち"

def test_special_characters():
    """Test function with special characters"""
    assert find_longest_substring("!@#$%^&*()!") == "!@#$%^&*()"