import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic_match():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    results = z_algorithm(text, pattern)
    assert results == [10], f"Expected [10], but got {results}"

def test_z_algorithm_multiple_matches():
    """Test multiple occurrences of the pattern"""
    text = "AAAAAAA"
    pattern = "AA"
    results = z_algorithm(text, pattern)
    assert results == [0, 1, 2, 3, 4, 5], f"Expected [0, 1, 2, 3, 4, 5], but got {results}"

def test_z_algorithm_no_match():
    """Test when pattern is not in text"""
    text = "ABCDEF"
    pattern = "XYZ"
    results = z_algorithm(text, pattern)
    assert results == [], f"Expected [], but got {results}"

def test_z_algorithm_edge_cases():
    """Test edge cases"""
    # Empty text
    assert z_algorithm("", "ABC") == []
    
    # Empty pattern
    assert z_algorithm("ABCDEF", "") == []
    
    # Single character match
    assert z_algorithm("ABCDEF", "D") == [3]

def test_z_algorithm_full_string_match():
    """Test when entire text matches the pattern"""
    text = "ABABAB"
    pattern = "ABABAB"
    results = z_algorithm(text, pattern)
    assert results == [0], f"Expected [0], but got {results}"