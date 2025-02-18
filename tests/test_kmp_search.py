import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array('AAAA') == [0, 1, 2, 3]
    assert compute_lps_array('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps_array('AABAACAABAA') == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == [9]
    assert kmp_search('AAAAABAAABA', 'AAABA') == [5, 6]
    assert kmp_search('hello world', 'world') == [6]

def test_kmp_search_multiple_occurrences():
    # Test multiple occurrences of pattern
    assert kmp_search('AAAAAAA', 'AA') == [0, 1, 2, 3, 4, 5]
    assert kmp_search('ABABABAB', 'ABAB') == [0, 2, 4]

def test_kmp_search_no_match():
    # Test scenarios with no matches
    assert kmp_search('hello world', 'python') == []
    assert kmp_search('', 'test') == []
    assert kmp_search('test', '') == []

def test_kmp_search_edge_cases():
    # Test edge cases and corner scenarios
    assert kmp_search('', '') == []
    assert kmp_search('a', 'a') == [0]
    assert kmp_search('abcdef', 'abcdef') == [0]
    assert kmp_search('abcdef', 'xyz') == []

def test_kmp_search_case_sensitive():
    # Test case sensitivity
    assert kmp_search('Hello World', 'hello') == []
    assert kmp_search('Hello World', 'World') == [6]