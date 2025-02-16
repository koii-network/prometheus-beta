import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("hello", "") == ""
    assert longest_common_subsequence("", "world") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("python", "python") == "python"

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_partial_match():
    """Test partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("Programming", "Programming") == "Programming"

def test_random_strings():
    """Test with longer random strings"""
    str1 = "ABCDGHLQWERTYU"
    str2 = "BCDGKLMNQRSTVYZ"
    result = longest_common_subsequence(str1, str2)
    assert result in str1 and result in str2

def test_different_lengths():
    """Test strings with significantly different lengths"""
    assert longest_common_subsequence("short", "a very long string with short in it") == "short"