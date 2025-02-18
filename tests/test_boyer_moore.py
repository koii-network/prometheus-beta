import pytest
from src.boyer_moore import boyer_moore_search

def test_boyer_moore_basic_search():
    """Test basic string matching"""
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_boyer_moore_multiple_matches():
    """Test finding multiple matches"""
    text = "ABABABCABC"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4, 7]

def test_boyer_moore_no_matches():
    """Test when pattern is not found"""
    text = "ABCDEF"
    pattern = "XYZ"
    assert boyer_moore_search(text, pattern) == []

def test_boyer_moore_whole_text_match():
    """Test when pattern matches entire text"""
    text = "HELLO"
    pattern = "HELLO"
    assert boyer_moore_search(text, pattern) == [0]

def test_boyer_moore_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "ABC"
    pattern = "ABCDEF"
    assert boyer_moore_search(text, pattern) == []

def test_boyer_moore_empty_text():
    """Test searching in an empty text"""
    text = ""
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == []

def test_boyer_moore_input_type_error():
    """Test type checking for inputs"""
    with pytest.raises(TypeError):
        boyer_moore_search(123, "ABC")
    
    with pytest.raises(TypeError):
        boyer_moore_search("ABC", 123)

def test_boyer_moore_empty_pattern():
    """Test empty pattern validation"""
    with pytest.raises(ValueError):
        boyer_moore_search("ABC", "")