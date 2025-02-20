import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic scenario with a clear longest common subsequence"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("AbC", "aBc") == "A"

def test_multiple_possible_lcs():
    """Test scenarios with multiple possible longest common subsequences"""
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result == "BCBA"  # One of the valid longest common subsequences

def test_numeric_strings():
    """Test with numeric strings"""
    assert longest_common_subsequence("123456", "234567") == "23456"

def test_longer_complex_sequence():
    """Test a more complex and longer sequence"""
    assert longest_common_subsequence(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
        "AZBYCXDWEVFUGTHSIRJQKPLOMN"
    ) == "ABCDEFGHIJKLMN"