import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test case 1: Simple repeating pattern
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    
    # Test case 2: Pattern with some repetition
    assert compute_lps_array("ABCAB") == [0, 0, 0, 1, 2]
    
    # Test case 3: Pattern with complex prefix-suffix relationship
    assert compute_lps_array("ABABCABAB") == [0, 0, 1, 2, 0, 1, 2, 3, 4]
    
    # Test case 4: Empty string
    assert compute_lps_array("") == []

def test_kmp_search_basic():
    # Basic matching scenarios
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    
    # Multiple occurrences
    assert kmp_search("AAAAAA", "AA") == [0, 1, 2, 3, 4]

def test_kmp_search_edge_cases():
    # Empty text
    assert kmp_search("", "ABC") == []
    
    # Empty pattern
    assert kmp_search("ABCDEF", "") == []
    
    # Pattern longer than text
    assert kmp_search("ABC", "ABCDEF") == []

def test_kmp_search_no_match():
    # No match scenarios
    assert kmp_search("ABCDEF", "XYZ") == []
    assert kmp_search("ABCDEF", "GHI") == []

def test_kmp_search_case_sensitive():
    # Case-sensitive matching
    assert kmp_search("AbCdEfG", "Cd") == []
    assert kmp_search("AbCdEfG", "Cd".lower()) == [2]

def test_kmp_search_special_characters():
    # Special characters and symbols
    assert kmp_search("Hello, world! Hello again!", "Hello") == [0, 14]
    assert kmp_search("a!b@c#d$e%f", "!b@c") == [1]