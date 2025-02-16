import pytest
from src.rabin_karp import rabin_karp_search

def test_rabin_karp_basic_match():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [9]

def test_rabin_karp_multiple_matches():
    """Test multiple matches in the text"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    assert rabin_karp_search(text, pattern) == [0, 10, 15]

def test_rabin_karp_no_match():
    """Test when pattern is not in text"""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert rabin_karp_search(text, pattern) == []

def test_rabin_karp_empty_text():
    """Test searching in an empty text"""
    text = ""
    pattern = "ABC"
    assert rabin_karp_search(text, pattern) == []

def test_rabin_karp_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "TOOLONGPATTERN"
    assert rabin_karp_search(text, pattern) == []

def test_rabin_karp_case_sensitivity():
    """Test case sensitivity"""
    text = "Hello World"
    pattern = "world"
    assert rabin_karp_search(text, pattern) == []

def test_rabin_karp_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        rabin_karp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        rabin_karp_search("text", ["pattern"])

def test_rabin_karp_empty_pattern():
    """Test empty pattern raises ValueError"""
    with pytest.raises(ValueError):
        rabin_karp_search("text", "")