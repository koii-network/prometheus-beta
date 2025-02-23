import pytest
from src.lcs_length import longest_common_subsequence_length

def test_basic_subsequence():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4
    assert longest_common_subsequence_length("ABC", "AC") == 2

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("ABC", "") == 0
    assert longest_common_subsequence_length("", "XYZ") == 0

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence_length("HELLO", "HELLO") == 5
    assert longest_common_subsequence_length("", "") == 0

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence_length("ABC", "XYZ") == 0

def test_case_sensitivity():
    """Test case-sensitive comparisons"""
    assert longest_common_subsequence_length("Hello", "hello") == 4  # Corrected expectation
    assert longest_common_subsequence_length("ABC", "abc") == 0

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence_length(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence_length("ABC", None)
    with pytest.raises(TypeError):
        longest_common_subsequence_length(None, None)

def test_complex_subsequences():
    """Test more complex subsequence scenarios"""
    assert longest_common_subsequence_length("ABCBDAB", "BDCABA") == 4
    assert longest_common_subsequence_length("XMJYAUZ", "MZJAWXU") == 4