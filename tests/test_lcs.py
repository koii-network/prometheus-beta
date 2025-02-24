import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test LCS with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test LCS with identical strings"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_common_subsequence():
    """Test strings with partial common subsequence"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BDAB"

def test_single_character_strings():
    """Test strings with single characters"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)
    with pytest.raises(TypeError):
        longest_common_subsequence([], "ABC")