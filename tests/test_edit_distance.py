import pytest
from src.edit_distance import edit_distance

def test_edit_distance_basic():
    """Test basic edit distance scenarios"""
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("saturday", "sunday") == 3
    assert edit_distance("cat", "cat") == 0

def test_edit_distance_empty_strings():
    """Test scenarios with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_edit_distance_different_lengths():
    """Test strings of different lengths"""
    assert edit_distance("abc", "abcd") == 1
    assert edit_distance("abcd", "abc") == 1

def test_edit_distance_complex():
    """Test more complex edit distance scenarios"""
    assert edit_distance("sunday", "saturday") == 3
    assert edit_distance("intention", "execution") == 5

def test_edit_distance_case_sensitivity():
    """Test case sensitivity of edit distance"""
    assert edit_distance("Hello", "hello") == 1
    assert edit_distance("Python", "python") == 1