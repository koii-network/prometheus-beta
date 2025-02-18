import pytest
from src.kmp_string_matching import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test cases for LPS array computation
    assert compute_lps_array('AAAA') == [0, 1, 2, 3]
    assert compute_lps_array('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps_array('AABAACAABAA') == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps_array('') == []

def test_kmp_search_basic():
    # Basic search tests
    assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == [10]
    assert kmp_search('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
    
def test_kmp_search_multiple_occurrences():
    # Multiple occurrences
    text = 'ABABABABA'
    pattern = 'ABA'
    assert kmp_search(text, pattern) == [0, 2, 4, 6]

def test_kmp_search_no_match():
    # No matches
    assert kmp_search('ABCDEFG', 'XYZ') == []
    assert kmp_search('', 'PATTERN') == []

def test_kmp_search_edge_cases():
    # Edge cases
    assert kmp_search('HELLO', '') == []
    assert kmp_search('', '') == []
    
def test_kmp_search_full_match():
    # Full text match
    assert kmp_search('PATTERN', 'PATTERN') == [0]

def test_kmp_search_case_sensitive():
    # Case-sensitive matching
    assert kmp_search('AbCdEfG', 'cd') == []
    assert kmp_search('AbCdEfG', 'Cd') == [2]