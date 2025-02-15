import pytest
from src.edit_distance import edit_distance

def test_edit_distance_basic():
    """Test basic edit distance scenarios"""
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("sunday", "saturday") == 3
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "hello") == 0

def test_edit_distance_empty_strings():
    """Test edit distance with empty strings"""
    assert edit_distance("", "abc") == 3
    assert edit_distance("xyz", "") == 3

def test_edit_distance_different_lengths():
    """Test edit distance for strings of different lengths"""
    assert edit_distance("cat", "cats") == 1
    assert edit_distance("dog", "dogs") == 1
    assert edit_distance("hi", "hello") == 3

def test_edit_distance_type_errors():
    """Test type error handling"""
    with pytest.raises(TypeError):
        edit_distance(123, "abc")
    with pytest.raises(TypeError):
        edit_distance("abc", 456)
    with pytest.raises(TypeError):
        edit_distance(None, "test")

def test_edit_distance_case_sensitivity():
    """Test edit distance is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1
    assert edit_distance("WORLD", "world") == 5