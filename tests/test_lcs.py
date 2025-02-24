import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test LCS with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test LCS when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test LCS when no common subsequence exists"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_match():
    """Test LCS with partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test LCS is case-sensitive"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAA", "AA") == "AA"

def test_input_types():
    """Test function handles string inputs"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", 456)