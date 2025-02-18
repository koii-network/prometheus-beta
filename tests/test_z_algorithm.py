import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic_match():
    """Test basic string matching"""
    text = "abcabcabc"
    pattern = "abc"
    assert z_algorithm(text, pattern) == [0, 3, 6]

def test_z_algorithm_no_match():
    """Test when pattern is not in text"""
    text = "abcdef"
    pattern = "xyz"
    assert z_algorithm(text, pattern) == []

def test_z_algorithm_single_char_match():
    """Test matching a single character"""
    text = "aaaaa"
    pattern = "a"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4]

def test_z_algorithm_empty_inputs():
    """Test with empty text or pattern"""
    assert z_algorithm("", "abc") == []
    assert z_algorithm("abc", "") == []

def test_z_algorithm_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "abc"
    pattern = "abcdef"
    assert z_algorithm(text, pattern) == []

def test_z_algorithm_overlapping_matches():
    """Test case with overlapping matches"""
    text = "anananan"
    pattern = "ananan"
    assert z_algorithm(text, pattern) == [0, 2, 4]