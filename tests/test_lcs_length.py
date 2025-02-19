import pytest
from src.lcs_length import longest_common_subsequence_length

def test_basic_lcs_length():
    assert longest_common_subsequence_length('abcde', 'ace') == 3
    assert longest_common_subsequence_length('abc', 'abc') == 3
    assert longest_common_subsequence_length('abc', 'def') == 0

def test_empty_strings():
    assert longest_common_subsequence_length('', 'abc') == 0
    assert longest_common_subsequence_length('abc', '') == 0
    assert longest_common_subsequence_length('', '') == 0

def test_partial_matches():
    assert longest_common_subsequence_length('abcdgh', 'aedfhr') == 3
    assert longest_common_subsequence_length('aggtab', 'gxtxayb') == 4

def test_case_sensitive():
    assert longest_common_subsequence_length('ABC', 'abc') == 0

def test_repeated_characters():
    assert longest_common_subsequence_length('aaaaaa', 'aa') == 2
    assert longest_common_subsequence_length('abcabcabc', 'abc') == 3

def test_long_sequences():
    s1 = 'ABCDGH' * 100
    s2 = 'AEDFHR' * 100
    assert longest_common_subsequence_length(s1, s2) == 3 * 100