import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_one_empty_string():
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""

def test_partially_overlapping_strings():
    assert longest_common_subsequence("ABCDE", "ACDE") == "ACDE"

def test_case_sensitivity():
    assert longest_common_subsequence("AbCdE", "aBcDe") == "bCe"

def test_long_strings():
    A = "ABCBDAB"
    B = "BDCABA"
    assert longest_common_subsequence(A, B) == "BCBA"