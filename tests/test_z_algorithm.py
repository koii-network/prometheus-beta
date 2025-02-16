import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching scenarios"""
    # Simple pattern in text
    assert z_algorithm("hello world", "o") == [4, 7]
    
    # Pattern at the start
    assert z_algorithm("hello world", "hello") == [0]
    
    # Pattern at the end
    assert z_algorithm("hello world", "world") == [6]
    
    # Multiple occurrences
    assert z_algorithm("banana", "ana") == [1, 3]

def test_no_match():
    """Test scenarios with no matches"""
    assert z_algorithm("hello world", "xyz") == []
    assert z_algorithm("", "pattern") == []
    assert z_algorithm("text", "") == []

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    # Entire text is the pattern
    assert z_algorithm("hello", "hello") == [0]
    
    # Pattern longer than text
    assert z_algorithm("hi", "hello") == []
    
    # Case sensitivity
    assert z_algorithm("Hello World", "world") == []
    assert z_algorithm("Hello World", "World") == [6]

def test_overlapping_matches():
    """Test scenarios with overlapping matches"""
    assert z_algorithm("aaaaa", "aa") == [0, 1, 2, 3]

def test_complex_patterns():
    """Test more complex pattern matching scenarios"""
    # Repeated characters
    assert z_algorithm("aabaabaab", "aab") == [0, 3, 6]
    
    # Longer text and pattern
    text = "abcabcabcabc"
    pattern = "abcabc"
    assert z_algorithm(text, pattern) == [0, 6]