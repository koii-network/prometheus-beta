import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"
    assert longest_common_subsequence("abc", "abc") == "abc"

def test_empty_string_cases():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("test", "") == ""
    assert longest_common_subsequence("", "test") == ""

def test_no_common_subsequence():
    """Test cases with no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_different_length_strings():
    """Test LCS with strings of different lengths"""
    # Note: There might be multiple valid LCS with the same length
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert len(result) == 4  # Length of LCS should be 4
    assert set(result).issubset(set("ABCBDAB")) and set(result).issubset(set("BDCABA"))

def test_case_sensitivity():
    """Test LCS is case-sensitive"""
    assert len(longest_common_subsequence("Abc", "abc")) == 0

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "test")
    with pytest.raises(TypeError):
        longest_common_subsequence("test", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)