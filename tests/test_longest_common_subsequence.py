import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_basic_lcs():
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    assert find_longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    assert find_longest_common_subsequence("abc", "def") == ""

def test_one_empty_string():
    assert find_longest_common_subsequence("", "hello") == ""
    assert find_longest_common_subsequence("world", "") == ""

def test_partial_match():
    assert find_longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    assert find_longest_common_subsequence("Hello", "hello") == ""

def test_subsequence_not_substring():
    assert find_longest_common_subsequence("ABCDE", "ACE") == "ACE"
    assert find_longest_common_subsequence("ABCDE", "ACD") == "ACD"