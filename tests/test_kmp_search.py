import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array('AAAA') == [0, 1, 2, 3]
    assert compute_lps_array('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps_array('AABAACAABAA') == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps_array('') == []

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
    assert kmp_search('ABCABCABC', 'ABC') == [0, 3, 6]
    assert kmp_search('HELLO WORLD', 'WORLD') == [6]

def test_kmp_search_no_match():
    # Tests for no matches
    assert kmp_search('HELLO', 'WORLD') == []
    assert kmp_search('abc', 'def') == []

def test_kmp_search_edge_cases():
    # Edge case tests
    assert kmp_search('', '') == []
    assert kmp_search('abc', '') == []
    assert kmp_search('', 'abc') == []
    assert kmp_search('abc', 'abcd') == []

def test_kmp_search_single_character():
    # Single character pattern tests
    assert kmp_search('AAAA', 'A') == [0, 1, 2, 3]
    assert kmp_search('ABCDE', 'C') == [2]

def test_kmp_search_error_handling():
    # Error handling tests
    with pytest.raises(TypeError):
        kmp_search(123, 'pattern')
    with pytest.raises(TypeError):
        kmp_search('text', 123)

def test_kmp_search_overlap():
    # Test overlapping matches
    assert kmp_search('AAAAA', 'AA') == [0, 1, 2, 3]

def test_kmp_search_case_sensitive():
    # Case sensitivity test
    assert kmp_search('AbcAbcAbc', 'abc') == []
    assert kmp_search('AbcAbcAbc', 'Abc') == [0, 3, 6]