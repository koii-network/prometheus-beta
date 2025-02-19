import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_common_subsequence():
    """Test common subsequence scenarios"""
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("abc", "") == 0
    assert longest_common_subsequence_length("", "xyz") == 0

def test_partial_match():
    """Test scenarios with partial matches"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence_length("ABC", "abc") == 0
    assert longest_common_subsequence_length("Hello", "hello") == 4  # Actually matches 4 characters

def test_longer_strings():
    """Test longer input strings"""
    test_str1 = "ABCBDAB"
    test_str2 = "BDCABA"
    assert longest_common_subsequence_length(test_str1, test_str2) == 4