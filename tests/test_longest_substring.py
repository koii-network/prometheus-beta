import pytest
from src.longest_substring import find_longest_substring

def test_basic_case():
    """Test basic functionality of the function"""
    assert find_longest_substring("abcabcbb") == "abc"

def test_all_unique_characters():
    """Test a string with all unique characters"""
    assert find_longest_substring("abcdefg") == "abcdefg"

def test_repeated_characters():
    """Test a string with repeated characters"""
    assert find_longest_substring("bbbbb") == "b"

def test_empty_string():
    """Test empty string input"""
    assert find_longest_substring("") == ""

def test_multiple_longest_substrings():
    """Test when multiple substrings have the same max length"""
    assert find_longest_substring("pwwkew") == "wke"

def test_case_sensitivity():
    """Test case-sensitive substring finding"""
    assert find_longest_substring("AbcA") == "Abc"

def test_mixed_characters():
    """Test mixed case and repeated characters"""
    assert find_longest_substring("aAabBcC") == "aAabBcC"

def test_unicode_characters():
    """Test with unicode characters"""
    assert find_longest_substring("hello世界") == "hello世界"