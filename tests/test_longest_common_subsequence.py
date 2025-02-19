import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_lcs():
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("", "abc") == 0
    assert longest_common_subsequence_length("abc", "") == 0

def test_different_length_strings():
    assert longest_common_subsequence_length("abcdgh", "aedfhr") == 3
    assert longest_common_subsequence_length("aggtab", "gxtxayb") == 4

def test_case_sensitivity():
    assert longest_common_subsequence_length("ABC", "abc") == 0
    assert longest_common_subsequence_length("Abc", "abc") == 1  # Only the 'c' matches
    assert longest_common_subsequence_length("aB", "ab") == 0
    assert longest_common_subsequence_length("aA", "aa") == 1

def test_repeated_characters():
    assert longest_common_subsequence_length("aaa", "aa") == 2
    assert longest_common_subsequence_length("aabb", "ab") == 2