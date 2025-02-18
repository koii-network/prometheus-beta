import pytest
from src.aho_corasick import AhoCorasick

def test_basic_search():
    """Test basic pattern matching"""
    patterns = ["he", "she", "his", "hers"]
    ac = AhoCorasick(patterns)
    text = "she sells seashells"
    
    results = ac.search(text)
    
    # Expected results: (0, "she"), (13, "he")
    assert len(results) == 2
    assert (0, "she") in results
    assert (13, "he") in results

def test_overlapping_patterns():
    """Test overlapping pattern matching"""
    patterns = ["ab", "abc", "bc"]
    ac = AhoCorasick(patterns)
    text = "abcde"
    
    results = ac.search(text)
    
    # Expected results: (0, "ab"), (0, "abc"), (1, "bc")
    assert len(results) == 3
    assert (0, "ab") in results
    assert (0, "abc") in results
    assert (1, "bc") in results

def test_multiple_occurrences():
    """Test multiple occurrences of patterns"""
    patterns = ["a", "ab"]
    ac = AhoCorasick(patterns)
    text = "ababa"
    
    results = ac.search(text)
    
    # Expected results should include multiple pattern matches
    assert len(results) == 6
    assert (0, "a") in results
    assert (1, "ab") in results
    assert (2, "a") in results
    assert (3, "a") in results
    assert (4, "a") in results

def test_no_matches():
    """Test scenario with no pattern matches"""
    patterns = ["hello", "world"]
    ac = AhoCorasick(patterns)
    text = "python programming"
    
    results = ac.search(text)
    
    assert len(results) == 0

def test_empty_input():
    """Test searching with empty text or patterns"""
    patterns = ["test"]
    ac = AhoCorasick(patterns)
    
    # Empty text
    results = ac.search("")
    assert len(results) == 0
    
    # Empty patterns
    ac_empty = AhoCorasick([])
    results = ac_empty.search("some text")
    assert len(results) == 0

def test_case_sensitivity():
    """Test case sensitivity of pattern matching"""
    patterns = ["Python", "python"]
    ac = AhoCorasick(patterns)
    text = "I love Python programming"
    
    results = ac.search(text)
    
    # Should only match "Python"
    assert len(results) == 1
    assert (7, "Python") in results