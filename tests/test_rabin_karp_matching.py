import pytest
from src.rabin_karp_matching import rabin_karp_search

def test_basic_pattern_matching():
    """Test basic pattern matching"""
    text = "hello world hello"
    pattern = "hello"
    assert rabin_karp_search(text, pattern) == [0, 12]

def test_no_match():
    """Test when pattern is not in text"""
    text = "hello world"
    pattern = "python"
    assert rabin_karp_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "short"
    pattern = "longer pattern"
    assert rabin_karp_search(text, pattern) == []

def test_empty_inputs():
    """Test empty text or pattern"""
    assert rabin_karp_search("", "test") == []
    assert rabin_karp_search("test", "") == []

def test_overlapping_patterns():
    """Test overlapping pattern matches"""
    text = "aaaaa"
    pattern = "aa"
    assert rabin_karp_search(text, pattern) == [0, 1, 2, 3]

def test_case_sensitive():
    """Test case sensitivity"""
    text = "Hello World Hello"
    pattern = "hello"
    assert rabin_karp_search(text, pattern) == []
    pattern = "Hello"
    assert rabin_karp_search(text, pattern) == [0, 12]

def test_single_character_pattern():
    """Test single character pattern matching"""
    text = "abcdefg"
    pattern = "c"
    assert rabin_karp_search(text, pattern) == [2]

def test_entire_text_as_pattern():
    """Test when entire text is the pattern"""
    text = "hello"
    pattern = "hello"
    assert rabin_karp_search(text, pattern) == [0]