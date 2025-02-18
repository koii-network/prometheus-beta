import pytest
from src.kmp_search import kmp_search, compute_lps

def test_compute_lps():
    # Test LPS computation for different patterns
    assert compute_lps('AAAA') == [0, 1, 2, 3]
    assert compute_lps('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps('AABAACAABAA') == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Basic search scenarios
    assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == [9]
    assert kmp_search('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
    assert kmp_search('ABRACADABRA', 'ABRA') == [0, 7]

def test_kmp_search_edge_cases():
    # Edge case scenarios
    assert kmp_search('', 'PATTERN') == []  # Empty text
    assert kmp_search('TEXT', '') == []  # Empty pattern
    assert kmp_search('HELLO', 'X') == []  # Pattern not in text
    assert kmp_search('AAAAA', 'AA') == [0, 1, 2, 3]  # Overlapping matches

def test_kmp_search_case_sensitive():
    # Case sensitivity check
    assert kmp_search('AbAbCdEfG', 'Ab') == [0, 2]
    assert kmp_search('AbAbCdEfG', 'ab') == []

def test_compute_lps_edge_cases():
    # Edge cases for LPS computation
    assert compute_lps('') == []
    assert compute_lps('A') == [0]
    assert compute_lps('ABCABCABC') == [0, 0, 0, 1, 2, 3, 4, 5, 6]