import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_subsequence():
    assert longest_common_subsequence_length("abcde", "ace") == 3

def test_no_common_subsequence():
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("abc", "") == 0
    assert longest_common_subsequence_length("", "xyz") == 0

def test_identical_strings():
    assert longest_common_subsequence_length("hello", "hello") == 5

def test_partial_overlap():
    assert longest_common_subsequence_length("abcdgh", "aedfhr") == 3

def test_case_sensitivity():
    assert longest_common_subsequence_length("Hello", "hello") == 1

def test_mixed_chars():
    assert longest_common_subsequence_length("stone", "longest") == 3

def test_single_char_match():
    assert longest_common_subsequence_length("a", "a") == 1
    assert longest_common_subsequence_length("a", "b") == 0