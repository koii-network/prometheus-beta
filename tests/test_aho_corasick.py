import pytest
from src.aho_corasick import AhoCorasick

def test_basic_pattern_matching():
    """Test basic multiple pattern matching"""
    patterns = ["he", "she", "his", "hers"]
    text = "she sells seashells by the seashore"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Expected matches
    expected_matches = [
        (0, "she"),
        (1, "he"),
        (4, "he")
    ]
    
    # Check if all expected matches are found
    assert set(results) == set(expected_matches)

def test_overlapping_patterns():
    """Test matching overlapping patterns"""
    patterns = ["ab", "abc", "bc"]
    text = "abcde"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Expected matches
    expected_matches = [
        (0, "ab"),
        (0, "abc"),
        (1, "bc")
    ]
    
    # Check if all expected matches are found
    assert set(results) == set(expected_matches)

def test_no_matches():
    """Test scenario with no pattern matches"""
    patterns = ["xyz", "123"]
    text = "abcde"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Expected empty result
    assert len(results) == 0

def test_repeated_patterns():
    """Test matching repeated patterns"""
    patterns = ["a", "aa"]
    text = "aaaa"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Expected matches
    expected_matches = [
        (0, "a"), (0, "aa"),
        (1, "a"), (1, "aa"),
        (2, "a"), (2, "aa"),
        (3, "a")
    ]
    
    # Check if all expected matches are found
    assert set(results) == set(expected_matches)

def test_empty_input():
    """Test with empty text and patterns"""
    patterns = []
    text = ""
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Expected empty result
    assert len(results) == 0