import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test case from classic KMP algorithm example
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_kmp_search_basic():
    # Basic matching scenarios
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("hello world", "hello") == [0]
    assert kmp_search("mississippi", "issip") == [4]

def test_kmp_search_multiple_matches():
    # Multiple matches in the text
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("AAAAAAA", "AA") == [0, 1, 2, 3, 4, 5]

def test_kmp_search_no_matches():
    # No matches scenario
    assert kmp_search("hello world", "python") == []

def test_kmp_search_edge_cases():
    # Edge case tests
    assert kmp_search("", "") == []
    assert kmp_search("abc", "") == []
    assert kmp_search("", "abc") == []

def test_kmp_search_case_sensitive():
    # Case sensitivity check
    assert kmp_search("Hello World", "hello") == []
    assert kmp_search("Hello World", "Hello") == [0]

def test_kmp_search_invalid_inputs():
    # Invalid input tests
    with pytest.raises(TypeError):
        kmp_search(123, "abc")
    with pytest.raises(TypeError):
        kmp_search("abc", 123)

def test_complete_text_match():
    # Entire text matches the pattern
    assert kmp_search("AAAA", "AAAA") == [0]