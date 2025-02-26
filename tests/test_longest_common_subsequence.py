import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("abc", "") == ""
    assert longest_common_subsequence("", "xyz") == ""

def test_one_character_match():
    """Test when only one character matches"""
    assert longest_common_subsequence("a", "a") == "a"
    assert longest_common_subsequence("abc", "def") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_type_error():
    """Test type checking"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", None)
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)