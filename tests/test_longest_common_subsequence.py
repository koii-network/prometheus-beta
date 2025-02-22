import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    """Test longest common subsequence with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("abc", "") == 0
    assert longest_common_subsequence_length("", "xyz") == 0

def test_substring_cases():
    """Test various string combination scenarios"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence_length("Hello", "hello") == 0
    assert longest_common_subsequence_length("python", "PYTHON") == 0

def test_special_characters():
    """Test strings with special characters"""
    assert longest_common_subsequence_length("a!b@c#", "a@b#c!") == 3
    assert longest_common_subsequence_length("123", "456") == 0