import pytest
from src.aho_corasick import AhoCorasick

def test_basic_string_matching():
    patterns = ["he", "she", "his", "hers"]
    text = "she sells seashells by the seashore"
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 3
    assert (1, "she") in results
    assert (22, "he") in results
    assert (25, "he") in results

def test_overlapping_patterns():
    patterns = ["ab", "abc", "bc"]
    text = "abcdef"
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 3
    assert (0, "ab") in results
    assert (0, "abc") in results
    assert (1, "bc") in results

def test_multiple_occurrences():
    patterns = ["a", "ab"]
    text = "ababa"
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 6
    assert results.count((0, "a")) == 2
    assert results.count((1, "a")) == 2
    assert results.count((3, "a")) == 2
    assert results.count((0, "ab")) == 1
    assert results.count((2, "ab")) == 1

def test_no_matches():
    patterns = ["hello", "world"]
    text = "python programming"
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 0

def test_empty_text():
    patterns = ["test", "abc"]
    text = ""
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 0

def test_empty_patterns():
    patterns = []
    text = "some text"
    ac = AhoCorasick(patterns)
    results = ac.search(text)
    
    assert len(results) == 0