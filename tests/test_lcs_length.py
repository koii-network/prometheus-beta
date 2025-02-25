import pytest
from src.lcs_length import longest_common_subsequence_length

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("abc", "") == 0
    assert longest_common_subsequence_length("", "xyz") == 0

def test_different_length_strings():
    """Test strings of different lengths"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_type_errors():
    """Test type handling for invalid inputs"""
    with pytest.raises(TypeError):
        longest_common_subsequence_length(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence_length("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence_length(None, "test")

def test_case_sensitivity():
    """Test case sensitivity of the function"""
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "ABC") == 0
    assert longest_common_subsequence_length("AbC", "abc") == 0

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_common_subsequence_length("AAAAAA", "AA") == 2
    assert longest_common_subsequence_length("ABABABAB", "BABA") == 4