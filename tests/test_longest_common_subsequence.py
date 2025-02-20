import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when both strings are identical."""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there's no common subsequence."""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_one_empty_string():
    """Test with one empty string."""
    assert longest_common_subsequence("", "HELLO") == ""
    assert longest_common_subsequence("HELLO", "") == ""

def test_both_empty_strings():
    """Test with both strings empty."""
    assert longest_common_subsequence("", "") == ""

def test_single_character_lcs():
    """Test LCS with single character matches."""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)

def test_lcs_case_sensitivity():
    """Test case sensitivity of the LCS algorithm."""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("AaBbCc", "AbC") == "AbC"