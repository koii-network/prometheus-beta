import pytest
from src.kmp_search import kmp_search, compute_lps

def test_compute_lps():
    # Test cases for LPS computation
    assert compute_lps("AAAA") == [0, 1, 2, 3]
    assert compute_lps("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps("ABABCABAB") == [0, 0, 1, 2, 0, 1, 2, 3, 4]

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("Hello world", "world") == [6]

def test_kmp_search_multiple_matches():
    # Multiple matches test
    assert kmp_search("AAAAAAAA", "AAA") == [0, 1, 2, 3, 4, 5]

def test_kmp_search_no_matches():
    # No matches test
    assert kmp_search("Hello world", "python") == []

def test_kmp_search_edge_cases():
    # Edge cases
    assert kmp_search("", "") == []
    assert kmp_search("abc", "") == []
    assert kmp_search("", "abc") == []

def test_kmp_search_invalid_input():
    # Invalid input tests
    with pytest.raises(TypeError):
        kmp_search(123, "abc")
    with pytest.raises(TypeError):
        kmp_search("abc", 123)
    
    with pytest.raises(ValueError):
        kmp_search("abc", "")