import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    """Test the LPS array computation for different patterns"""
    # Simple pattern
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    
    # Pattern with repeated subsequences
    assert compute_lps_array("ABCABCABC") == [0, 0, 0, 1, 2, 3, 4, 5, 6]
    
    # More complex pattern
    assert compute_lps_array("ABABACA") == [0, 0, 1, 2, 3, 0, 1]

def test_kmp_search_basic():
    """Test basic string matching scenarios"""
    # Simple match
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    
    # Multiple matches
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    
    # No matches
    assert kmp_search("ABCDEF", "XYZ") == []

def test_kmp_search_edge_cases():
    """Test edge cases for string matching"""
    # Pattern longer than text
    assert kmp_search("ABC", "ABCDEF") == []
    
    # Pattern same as text
    assert kmp_search("ABCDEF", "ABCDEF") == [0]
    
    # Empty pattern
    with pytest.raises(ValueError):
        kmp_search("ABCDEF", "")
    
    # Empty text
    with pytest.raises(ValueError):
        kmp_search("", "ABC")

def test_kmp_search_type_errors():
    """Test type validation"""
    # Non-string inputs
    with pytest.raises(TypeError):
        kmp_search(123, "ABC")
    
    with pytest.raises(TypeError):
        kmp_search("ABC", 123)

def test_kmp_search_special_characters():
    """Test matching with special characters and spaces"""
    # With spaces and special characters
    assert kmp_search("Hello, hello world! Hello again!", "hello") == [7, 20]
    
    # With mixed case
    assert kmp_search("Hello, HELLO world! hElLo again!", "hello") == [0, 7, 20]

def test_kmp_search_single_character():
    """Test matching with single character patterns"""
    # Single character multiple times
    assert kmp_search("AAAAA", "A") == [0, 1, 2, 3, 4]
    
    # Single character no match
    assert kmp_search("BBBBB", "A") == []