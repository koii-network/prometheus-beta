import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Test basic pattern matching
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("ABABABCABABABCABABABC", "ABABC") == [4, 14]
    assert kmp_search("Hello, world!", "world") == [7]

def test_kmp_search_no_match():
    # Test scenarios with no matches
    assert kmp_search("ABCDEF", "XYZ") == []
    assert kmp_search("Hello", "hello") == []  # Case-sensitive

def test_kmp_search_edge_cases():
    # Test edge cases
    assert kmp_search("", "") == []
    assert kmp_search("ABC", "") == []
    assert kmp_search("ABC", "ABC") == [0]

def test_kmp_search_input_validation():
    # Test input validation
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    
    with pytest.raises(ValueError):
        kmp_search("text", "")