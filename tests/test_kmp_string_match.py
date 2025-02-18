import pytest
from src.kmp_string_match import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Basic string matching
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    assert kmp_search("AAAAABAAABA", "AAABA") == [1, 6]
    assert kmp_search("hello world", "o w") == [4]

def test_kmp_search_no_match():
    # No matches scenario
    assert kmp_search("hello world", "xyz") == []

def test_kmp_search_multiple_matches():
    # Multiple matches
    assert kmp_search("AAAAAAA", "AA") == [0, 1, 2, 3, 4, 5]

def test_kmp_search_edge_cases():
    # Empty text
    assert kmp_search("", "pattern") == []
    
    # Pattern longer than text
    assert kmp_search("short", "longer pattern") == []

def test_kmp_search_invalid_input():
    # Invalid input types
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        kmp_search("text", 456)

def test_kmp_search_empty_pattern():
    # Empty pattern should raise an error
    with pytest.raises(ValueError):
        kmp_search("text", "")