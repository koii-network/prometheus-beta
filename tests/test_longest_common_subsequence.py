import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_lcs_basic():
    """Test basic LCS scenarios"""
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_edge_cases():
    """Test edge cases like empty strings and different length inputs"""
    assert find_longest_common_subsequence("", "") == ""
    assert find_longest_common_subsequence("ABC", "") == ""
    assert find_longest_common_subsequence("", "XYZ") == ""

def test_lcs_identical_strings():
    """Test when strings are identical"""
    assert find_longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert find_longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError):
        find_longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        find_longest_common_subsequence("ABC", None)

def test_lcs_case_sensitive():
    """Test case sensitivity"""
    assert find_longest_common_subsequence("abcde", "ABCDE") == ""
    assert find_longest_common_subsequence("aA", "bA") == "A"