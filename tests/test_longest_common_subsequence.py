import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_lcs_basic():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_edge_cases():
    # Empty strings
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_lcs_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_partial_match():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_lcs_with_repeated_characters():
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCBDAB", "ABCBDAB") == "ABCBDAB"