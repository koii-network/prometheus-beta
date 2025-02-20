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

def test_single_character_match():
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_multiple_possible_lcs():
    # When multiple LCS of same length exist, return the first one found
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result in ["BDAB", "BCBA"]  # Both are valid 4-character LCS

def test_case_differences():
    # In the original problem description, LCS is not case-sensitive
    assert longest_common_subsequence("Hello", "hello") in ["ello", "Hell"]