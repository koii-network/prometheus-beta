import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_one_empty_string():
    assert longest_common_subsequence("", "ABCD") == ""
    assert longest_common_subsequence("ABCD", "") == ""

def test_partial_match():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    assert longest_common_subsequence("hello", "HELLO") == ""

def test_unicode_strings():
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こん"