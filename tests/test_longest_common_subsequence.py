import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_empty_strings():
    """Test handling of empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_partial_matches():
    """Test partial matching scenarios"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_one_character_match():
    """Test scenarios with single character matches"""
    assert longest_common_subsequence("Z", "Z") == "Z"
    assert longest_common_subsequence("ABCDE", "AXCYE") == "ACE"