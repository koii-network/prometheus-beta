import pytest
from src.rabin_karp import rabin_karp_search

def test_basic_pattern_matching():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [9]

def test_multiple_occurrences():
    """Test finding multiple occurrences of a pattern"""
    text = "AAAAAAAA"
    pattern = "AAA"
    assert rabin_karp_search(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_no_match():
    """Test when pattern is not in text"""
    text = "ABCDEF"
    pattern = "XYZ"
    assert rabin_karp_search(text, pattern) == []

def test_empty_pattern():
    """Test with empty pattern"""
    text = "HELLO WORLD"
    pattern = ""
    assert rabin_karp_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "LONGER PATTERN"
    assert rabin_karp_search(text, pattern) == []

def test_input_type_validation():
    """Test input type validation"""
    with pytest.raises(TypeError):
        rabin_karp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        rabin_karp_search("text", 456)

def test_case_sensitive():
    """Test case sensitivity"""
    text = "Hello World"
    pattern = "world"
    assert rabin_karp_search(text, pattern) == []
    assert rabin_karp_search(text, "World") == [6]

def test_entire_text_match():
    """Test when entire text matches the pattern"""
    text = "HELLO"
    pattern = "HELLO"
    assert rabin_karp_search(text, pattern) == [0]