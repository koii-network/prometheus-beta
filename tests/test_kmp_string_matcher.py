import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("ABABCABAB") == [0, 0, 1, 2, 0, 1, 2, 3, 4]

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("ABCXABCDABXABCDABCDABCY", "ABCDABCY") == [15]

def test_kmp_search_multiple_matches():
    # Test multiple matches
    text = "AAAAAAAA"
    pattern = "AAA"
    assert kmp_search(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_kmp_search_no_matches():
    # Test when pattern is not found
    assert kmp_search("ABCDEF", "XYZ") == []

def test_kmp_search_edge_cases():
    # Edge case tests
    assert kmp_search("", "") == []
    assert kmp_search("ABC", "") == []
    assert kmp_search("ABC", "ABC") == [0]

def test_kmp_search_invalid_input():
    # Invalid input tests
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    
    with pytest.raises(ValueError):
        kmp_search("text", "")