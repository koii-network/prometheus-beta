import pytest
from src.string_matching import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCABCD") == [0, 0, 0, 1, 2, 3, 0]
    assert compute_lps_array("") == []

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    
def test_kmp_search_multiple_matches():
    # Test multiple matches
    text = "ABABABAB"
    pattern = "ABAB"
    assert kmp_search(text, pattern) == [0, 2, 4]

def test_kmp_search_no_match():
    # Test when pattern is not found
    assert kmp_search("ABCDEF", "XYZ") == []

def test_kmp_search_empty_pattern():
    # Test with empty pattern
    assert kmp_search("ABCDEF", "") == []

def test_kmp_search_empty_text():
    # Test with empty text
    assert kmp_search("", "ABC") == []

def test_kmp_search_full_text_match():
    # Test when entire text matches the pattern
    assert kmp_search("AAAAA", "AAAAA") == [0]

def test_case_sensitive():
    # Test case sensitivity
    assert kmp_search("AbCdEfG", "cd") == []
    assert kmp_search("AbCdEfG", "Cd") == []
    assert kmp_search("AbCdEfG", "Cd".lower()) == [2]