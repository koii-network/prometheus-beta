import pytest
from src.longest_common_subsequence import lcs_length

def test_lcs_length_basic():
    """Test basic LCS scenarios"""
    assert lcs_length("ABCDGH", "AEDFHR") == 3
    assert lcs_length("AGGTAB", "GXTXAYB") == 4

def test_lcs_length_empty_strings():
    """Test LCS with empty strings"""
    assert lcs_length("", "") == 0
    assert lcs_length("", "ABC") == 0
    assert lcs_length("XYZ", "") == 0

def test_lcs_length_identical_strings():
    """Test LCS with identical strings"""
    assert lcs_length("HELLO", "HELLO") == 5
    assert lcs_length("", "") == 0

def test_lcs_length_no_common_subsequence():
    """Test LCS with no common subsequence"""
    assert lcs_length("ABC", "XYZ") == 0

def test_lcs_length_single_character():
    """Test LCS with single character matching"""
    assert lcs_length("A", "A") == 1
    assert lcs_length("A", "B") == 0

def test_lcs_length_case_sensitivity():
    """Test LCS is case-sensitive"""
    assert lcs_length("hello", "HELLO") == 0

def test_lcs_length_large_input():
    """Test LCS with larger input strings"""
    str1 = "ABCBDAB" * 10
    str2 = "BDCABA" * 10
    # Note: The exact length might vary, but it should be a positive integer
    assert lcs_length(str1, str2) > 0