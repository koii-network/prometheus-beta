import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test behavior with empty strings"""
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_partial_match():
    """Test scenarios with partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("abcDE", "abcde") == "abc"

def test_long_strings():
    """Test with longer strings"""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "AZCBDEFGHIJKLMNOPQRST"
    assert longest_common_subsequence(str1, str2) == "ABCDEFGHIJKLMNOPQRST"