import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test cases for LPS array computation
    assert compute_lps_array('AAAA') == [0, 1, 2, 3]
    assert compute_lps_array('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps_array('AABAACAABAA') == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps_array('') == []

def test_kmp_search_basic():
    # Basic search scenarios
    assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == [9]
    assert kmp_search('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
    assert kmp_search('hello world', 'o') == [4, 7]

def test_kmp_search_multiple_occurrences():
    # Multiple occurrences of pattern
    text = 'AAAAAAAA'
    pattern = 'AAA'
    assert kmp_search(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_kmp_search_no_match():
    # No match scenarios
    assert kmp_search('hello world', 'xyz') == []
    assert kmp_search('', 'test') == []

def test_kmp_search_edge_cases():
    # Edge cases
    assert kmp_search('hello', '') == []
    assert kmp_search('', '') == []

def test_kmp_search_invalid_input():
    # Invalid input type
    with pytest.raises(TypeError):
        kmp_search(123, 'test')
    with pytest.raises(TypeError):
        kmp_search('hello', 123)

def test_kmp_search_case_sensitive():
    # Case sensitivity check
    assert kmp_search('Hello World', 'world') == []
    assert kmp_search('Hello World', 'World') == [6]