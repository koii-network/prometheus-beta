import pytest
from src.lcs import longest_common_subsequence

def test_lcs_basic():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"

def test_lcs_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_one_empty_string():
    assert longest_common_subsequence("", "ABCD") == ""
    assert longest_common_subsequence("ABCD", "") == ""

def test_lcs_multiple_subsequences():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_case_sensitive():
    assert longest_common_subsequence("Hello", "hello") == ""

def test_lcs_long_strings():
    X = "ABCBDAB"
    Y = "BDCABA"
    assert longest_common_subsequence(X, Y) == "BCBA"