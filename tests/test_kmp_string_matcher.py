import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    assert kmp_search("AAAAABAAABA", "AAABA") == [1, 6]
    assert kmp_search("hello world", "world") == [6]
    assert kmp_search("hello world", "xyz") == []

def test_kmp_search_multiple_occurrences():
    # Test multiple occurrences
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    assert kmp_search(text, pattern) == [0, 9, 12]

def test_kmp_search_edge_cases():
    # Edge case tests
    assert kmp_search("", "") == []
    assert kmp_search("abc", "") == []
    assert kmp_search("", "abc") == []

def test_kmp_search_error_handling():
    # Error handling tests
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    with pytest.raises(ValueError):
        kmp_search("text", "")