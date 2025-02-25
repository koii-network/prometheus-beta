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
    """Test when strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_multiple_subsequences():
    """Test scenarios with multiple possible subsequences"""
    assert longest_common_subsequence("ABCDGH", "ABCDFH") == "ABCFH"

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", [1, 2, 3])
    
    with pytest.raises(ValueError):
        longest_common_subsequence(None, "abc")
    
    with pytest.raises(ValueError):
        longest_common_subsequence("abc", None)