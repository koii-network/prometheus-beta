import pytest
from src.lcs import longest_common_subsequence

def test_lcs_basic():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_edge_cases():
    """Test edge cases"""
    # Empty string cases
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_lcs_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_partial_match():
    """Test partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_lcs_with_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCDE", "ABCDE") == "ABCDE"