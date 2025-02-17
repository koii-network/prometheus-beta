import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_partial_common_subsequence():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    assert longest_common_subsequence("Hello", "hello") == ""

def test_repeated_characters():
    assert longest_common_subsequence("AAAA", "AA") == "AA"
    assert longest_common_subsequence("ABABABAB", "BABABABA") == "BABABA"