import pytest
from src.z_algorithm import z_algorithm

def test_basic_pattern_matching():
    """Test basic pattern matching"""
    text = "hello world hello"
    pattern = "hello"
    assert z_algorithm(text, pattern) == [0, 12]

def test_no_occurrences():
    """Test when pattern is not in text"""
    text = "world python"
    pattern = "java"
    assert z_algorithm(text, pattern) == []

def test_multiple_overlapping_occurrences():
    """Test multiple overlapping occurrences"""
    text = "aaaaa"
    pattern = "aa"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3]

def test_single_character_pattern():
    """Test pattern with single character"""
    text = "abcdefg"
    pattern = "c"
    assert z_algorithm(text, pattern) == [2]

def test_pattern_equals_text():
    """Test when pattern is same as text"""
    text = "python"
    pattern = "python"
    assert z_algorithm(text, pattern) == [0]

def test_empty_inputs_raise_error():
    """Test that empty inputs raise ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("", "test")
    with pytest.raises(ValueError):
        z_algorithm("test", "")
    with pytest.raises(ValueError):
        z_algorithm("", "")

def test_non_string_inputs_raise_error():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError):
        z_algorithm(123, "test")
    with pytest.raises(TypeError):
        z_algorithm("test", 456)
    with pytest.raises(TypeError):
        z_algorithm(None, None)