import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when input strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when there is no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_empty_strings():
    """Test handling of empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("abc", "") == ""
    assert longest_common_subsequence("", "xyz") == ""

def test_one_character_common():
    """Test when only one character is common"""
    assert longest_common_subsequence("a", "a") == "a"
    assert longest_common_subsequence("abc", "cde") == "c"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "abc")

def test_case_sensitivity():
    """Test case sensitivity of the LCS"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("ABC", "abc") == ""

def test_complex_lcs():
    """Test a more complex longest common subsequence"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"