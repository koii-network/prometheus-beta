import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_lcs_basic_scenarios():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("ABC", "") == ""

def test_lcs_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_partial_matches():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_lcs_case_sensitivity():
    assert longest_common_subsequence("Hello", "hello") == ""

def test_lcs_mixed_characters():
    assert longest_common_subsequence("a1b2c3", "1a2b3c") == "123"

def test_lcs_unicode_characters():
    assert longest_common_subsequence("café", "caféin") == "café"