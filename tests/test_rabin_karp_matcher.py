import pytest
from src.rabin_karp_matcher import rabin_karp_search

def test_basic_pattern_match():
    """Test basic pattern matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [9]

def test_multiple_pattern_matches():
    """Test when pattern appears multiple times"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    assert rabin_karp_search(text, pattern) == [0, 10]

def test_pattern_not_found():
    """Test when pattern is not in text"""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert rabin_karp_search(text, pattern) == []

def test_empty_text():
    """Test with empty text"""
    text = ""
    pattern = "TEST"
    assert rabin_karp_search(text, pattern) == []

def test_empty_pattern():
    """Test with empty pattern"""
    text = "HELLO WORLD"
    pattern = ""
    assert rabin_karp_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "VERYLONGPATTERN"
    assert rabin_karp_search(text, pattern) == []

def test_case_sensitive():
    """Test case sensitivity"""
    text = "Hello World"
    pattern = "world"
    assert rabin_karp_search(text, pattern) == []

def test_full_text_match():
    """Test when entire text matches the pattern"""
    text = "EXACTMATCH"
    pattern = "EXACTMATCH"
    assert rabin_karp_search(text, pattern) == [0]