import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_one_character_common():
    """Test when only one character is common"""
    assert longest_common_subsequence("ABCD", "WXYA") == "A"

def test_type_error():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "ABC")

def test_case_sensitivity():
    """Test case sensitivity of LCS"""
    assert longest_common_subsequence("AbCdE", "aBcDE") == "bCdE"

def test_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"