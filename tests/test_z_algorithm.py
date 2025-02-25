import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching scenario"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert z_algorithm(text, pattern) == [10]

def test_multiple_matches():
    """Test scenario with multiple pattern matches"""
    text = "AAAAAAAA"
    pattern = "AAA"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_no_matches():
    """Test scenario with no pattern matches"""
    text = "ABCDEF"
    pattern = "XYZ"
    assert z_algorithm(text, pattern) == []

def test_pattern_equals_text():
    """Test when pattern is exactly the same as text"""
    text = "HELLO"
    pattern = "HELLO"
    assert z_algorithm(text, pattern) == [0]

def test_empty_input_raises_error():
    """Test that empty inputs raise a ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("", "PATTERN")
    
    with pytest.raises(ValueError):
        z_algorithm("TEXT", "")

def test_non_string_input_raises_error():
    """Test that non-string inputs raise a TypeError"""
    with pytest.raises(TypeError):
        z_algorithm(123, "PATTERN")
    
    with pytest.raises(TypeError):
        z_algorithm("TEXT", 456)

def test_case_sensitive():
    """Test that string matching is case-sensitive"""
    text = "AbcAbcABC"
    pattern = "abc"
    assert z_algorithm(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "VERYLONGPATTERN"
    assert z_algorithm(text, pattern) == []