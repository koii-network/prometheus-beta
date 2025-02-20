import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_subsequence():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"

def test_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_common_subsequence():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    assert longest_common_subsequence("", "") == ""

def test_one_empty_string():
    assert longest_common_subsequence("HELLO", "") == ""
    assert longest_common_subsequence("", "WORLD") == ""

def test_different_length_strings():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitive():
    assert longest_common_subsequence("Hello", "hello") == ""