import pytest
from src.edit_distance import edit_distance

def test_same_strings():
    """Test when both strings are identical"""
    assert edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test handling of empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_basic_transformations():
    """Test basic edit distance scenarios"""
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("sunday", "saturday") == 3

def test_case_sensitivity():
    """Test case-sensitive comparisons"""
    assert edit_distance("Hello", "hello") == 1

def test_different_length_strings():
    """Test strings of different lengths"""
    assert edit_distance("short", "shorter") == 2
    assert edit_distance("longer", "long") == 2

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        edit_distance(123, "string")
    with pytest.raises(TypeError):
        edit_distance("string", [1, 2, 3])
    with pytest.raises(TypeError):
        edit_distance(None, "test")

def test_complex_transformations():
    """Test more complex string transformations"""
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("book", "back") == 2