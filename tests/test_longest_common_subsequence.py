import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when both strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when there is no common subsequence"""
    assert longest_common_subsequence("abc", "def") == ""

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("abc", "") == ""
    assert longest_common_subsequence("", "xyz") == ""

def test_one_character_common():
    """Test with just one common character"""
    assert longest_common_subsequence("abc", "cde") == "c"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "abc")