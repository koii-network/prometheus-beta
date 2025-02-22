import pytest
from src.aho_corasick import AhoCorasick

def test_single_pattern_match():
    """Test matching a single pattern"""
    ac = AhoCorasick(["hello"])
    matches = ac.find_matches("hello world")
    assert matches == {0: {"hello"}}

def test_multiple_pattern_match():
    """Test matching multiple patterns"""
    ac = AhoCorasick(["he", "she", "his"])
    matches = ac.find_matches("she sells seashells")
    assert matches == {0: {"she"}, 8: {"he"}}

def test_overlapping_patterns():
    """Test matching overlapping patterns"""
    ac = AhoCorasick(["ab", "bc", "abc"])
    matches = ac.find_matches("abcde")
    assert matches == {0: {"ab"}, 1: {"bc", "abc"}}

def test_repeated_matches():
    """Test matching repeated patterns"""
    ac = AhoCorasick(["a", "aa"])
    matches = ac.find_matches("aaaa")
    expected = {0: {"a", "aa"}, 1: {"a", "aa"}, 2: {"a", "aa"}, 3: {"a"}}
    assert matches == expected

def test_no_matches():
    """Test text with no matches"""
    ac = AhoCorasick(["hello", "world"])
    matches = ac.find_matches("python")
    assert matches == {}

def test_empty_text():
    """Test searching in an empty text"""
    ac = AhoCorasick(["test"])
    matches = ac.find_matches("")
    assert matches == {}

def test_empty_patterns():
    """Test with no patterns"""
    ac = AhoCorasick([])
    matches = ac.find_matches("some text")
    assert matches == {}

def test_case_sensitivity():
    """Test case-sensitive matching"""
    ac = AhoCorasick(["Hello", "hello"])
    matches = ac.find_matches("hello Hello")
    assert matches == {0: {"hello"}, 6: {"Hello"}}

def test_complex_multiple_matches():
    """Test complex scenario with multiple matches"""
    ac = AhoCorasick(["ab", "bc", "cd", "de"])
    matches = ac.find_matches("abcde")
    expected = {0: {"ab"}, 1: {"bc"}, 2: {"cd"}, 3: {"de"}}
    assert matches == expected