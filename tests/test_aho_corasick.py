import pytest
from src.aho_corasick import AhoCorasick

def test_basic_pattern_matching():
    """Test basic pattern matching"""
    patterns = ["he", "she", "his", "hers"]
    text = "she sells seashells by the seashore"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    # Check expected matches
    expected = [
        (0, "she"),   # "she" at the start
        (10, "he"),   # "he" in "seashells"
        (3, "he")     # "he" in "shells"
    ]
    
    assert set(results) == set(expected), f"Expected {expected}, but got {results}"

def test_overlapping_patterns():
    """Test overlapping pattern matching"""
    patterns = ["ab", "abc", "bc"]
    text = "abcde"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    expected = [
        (0, "ab"),
        (0, "abc"),
        (1, "bc")
    ]
    
    assert set(results) == set(expected), f"Expected {expected}, but got {results}"

def test_no_matches():
    """Test scenario with no matches"""
    patterns = ["hello", "world"]
    text = "python is awesome"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    assert len(results) == 0, f"Expected no matches, but got {results}"

def test_multiple_occurrences():
    """Test multiple occurrences of patterns"""
    patterns = ["a", "ab"]
    text = "ababa"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    expected = [
        (0, "a"),
        (0, "ab"),
        (1, "a"),
        (2, "a"),
        (2, "ab"),
        (3, "a")
    ]
    
    assert set(results) == set(expected), f"Expected {expected}, but got {results}"

def test_empty_input():
    """Test empty input text"""
    patterns = ["test"]
    text = ""
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    assert len(results) == 0, f"Expected no matches for empty text, but got {results}"

def test_empty_patterns():
    """Test with empty patterns list"""
    patterns = []
    text = "some text"
    ac = AhoCorasick(patterns)
    
    results = ac.search(text)
    
    assert len(results) == 0, f"Expected no matches with empty patterns, but got {results}"