import pytest
from src.aho_corasick import AhoCorasick

def test_single_pattern_match():
    """Test matching a single pattern in a text."""
    ac = AhoCorasick(["hello"])
    matches = ac.search("hello world")
    assert matches == [(0, "hello")]

def test_multiple_pattern_match():
    """Test matching multiple patterns in a text."""
    ac = AhoCorasick(["he", "she", "his", "hers"])
    matches = ac.search("she sells seashells")
    assert set(matches) == {(0, "she"), (4, "he")}

def test_overlapping_patterns():
    """Test matching overlapping patterns."""
    ac = AhoCorasick(["ab", "abc", "bc"])
    matches = ac.search("abcde")
    assert set(matches) == {(0, "ab"), (0, "abc"), (1, "bc")}

def test_no_matches():
    """Test when no patterns are found."""
    ac = AhoCorasick(["cat", "dog"])
    matches = ac.search("bird")
    assert matches == []

def test_multiple_occurrences():
    """Test finding multiple occurrences of the same pattern."""
    ac = AhoCorasick(["aa"])
    matches = ac.search("aaaa")
    assert matches == [(0, "aa"), (1, "aa"), (2, "aa")]

def test_empty_text():
    """Test searching in an empty text."""
    ac = AhoCorasick(["test"])
    matches = ac.search("")
    assert matches == []

def test_empty_patterns():
    """Test with an empty list of patterns."""
    ac = AhoCorasick([])
    matches = ac.search("hello world")
    assert matches == []