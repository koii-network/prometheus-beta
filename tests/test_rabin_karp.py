import pytest
from src.rabin_karp import rabin_karp_search

def test_basic_string_matching():
    """Test basic string matching scenario"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [10]

def test_multiple_occurrences():
    """Test finding multiple occurrences of a pattern"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    assert rabin_karp_search(text, pattern) == [0, 2, 10, 15]

def test_no_match():
    """Test when pattern is not in text"""
    text = "Hello, world!"
    pattern = "python"
    assert rabin_karp_search(text, pattern) == []

def test_single_character_pattern():
    """Test matching a single character pattern"""
    text = "hello"
    pattern = "l"
    assert rabin_karp_search(text, pattern) == [2, 3]

def test_empty_text():
    """Test searching in an empty text"""
    text = ""
    pattern = "abc"
    assert rabin_karp_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "short"
    pattern = "longer than text"
    assert rabin_karp_search(text, pattern) == []

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        rabin_karp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        rabin_karp_search("text", 456)

def test_empty_pattern():
    """Test handling of empty pattern"""
    with pytest.raises(ValueError):
        rabin_karp_search("text", "")