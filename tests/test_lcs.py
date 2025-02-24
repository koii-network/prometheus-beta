import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_sequences():
    """Test LCS with empty sequences"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_sequences():
    """Test when sequences are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there is no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_single_character_match():
    """Test LCS with single character matches"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("AbC", "aBc") == ""

def test_longer_complex_sequences():
    """Test more complex and longer sequences"""
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result in ["BDAB"]  # Multiple valid LCS can exist