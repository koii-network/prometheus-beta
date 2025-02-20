import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test LCS with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("hello", "") == ""
    assert longest_common_subsequence("", "world") == ""

def test_identical_strings():
    """Test LCS with identical strings"""
    assert longest_common_subsequence("python", "python") == "python"

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_single_character_lcs():
    """Test LCS with single character"""
    assert longest_common_subsequence("a", "a") == "a"
    assert longest_common_subsequence("abc", "cde") == "c"

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", ["list"])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)