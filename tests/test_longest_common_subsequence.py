import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_edge_cases():
    """Test edge cases like empty strings and single character strings"""
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_no_common_subsequence():
    """Test scenario with no common subsequence"""
    assert longest_common_subsequence("XYZ", "ABC") == ""

def test_type_errors():
    """Test type error handling"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)