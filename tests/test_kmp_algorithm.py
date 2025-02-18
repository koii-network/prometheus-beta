import pytest
from src.kmp_algorithm import kmp_search, compute_lps

def test_compute_lps():
    # Test cases for LPS computation
    assert compute_lps("AAAA") == [0, 1, 2, 3]
    assert compute_lps("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps("") == []

def test_kmp_search_basic():
    # Basic search scenarios
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    assert kmp_search("AAAAABAAABA", "AAABA") == [1, 6]
    assert kmp_search("Hello world", "world") == [6]
    assert kmp_search("Hello world", "python") == []

def test_kmp_search_edge_cases():
    # Edge cases
    assert kmp_search("", "") == []
    assert kmp_search("Hello", "") == []
    assert kmp_search("", "Hello") == []
    
    # Overlapping matches
    assert kmp_search("AAAAA", "AA") == [0, 1, 2, 3]

def test_kmp_search_multiple_occurrences():
    # Multiple occurrences and repeating patterns
    text = "ABABABABAB"
    pattern = "ABAB"
    assert kmp_search(text, pattern) == [0, 2, 4, 6]

def test_kmp_search_case_sensitive():
    # Case sensitivity test
    assert kmp_search("Hello World", "world") == []
    assert kmp_search("Hello World", "World") == [6]