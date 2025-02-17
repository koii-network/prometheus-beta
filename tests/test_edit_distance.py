import pytest
from src.edit_distance import edit_distance

def test_edit_distance_same_string():
    """Test edit distance between identical strings"""
    assert edit_distance("hello", "hello") == 0

def test_edit_distance_different_lengths():
    """Test edit distance between strings of different lengths"""
    assert edit_distance("kitten", "sitting") == 3

def test_edit_distance_empty_strings():
    """Test edit distance with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_edit_distance_single_character():
    """Test edit distance with single character changes"""
    assert edit_distance("cat", "bat") == 1
    assert edit_distance("dog", "dig") == 1

def test_edit_distance_multiple_operations():
    """Test edit distance requiring multiple operations"""
    assert edit_distance("sunday", "saturday") == 3

def test_edit_distance_case_sensitive():
    """Test edit distance is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1

def test_edit_distance_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        edit_distance(123, "hello")
    with pytest.raises(TypeError):
        edit_distance("hello", ["world"])
    with pytest.raises(TypeError):
        edit_distance(None, None)