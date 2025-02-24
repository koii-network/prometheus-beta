import pytest
from src.edit_distance import calculate_edit_distance

def test_identical_strings():
    """Test that identical strings have edit distance of 0"""
    assert calculate_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test edit distance between empty strings"""
    assert calculate_edit_distance("", "") == 0

def test_one_empty_string():
    """Test edit distance with one empty string"""
    assert calculate_edit_distance("hello", "") == 5
    assert calculate_edit_distance("", "world") == 5

def test_different_strings():
    """Test edit distance for different strings"""
    assert calculate_edit_distance("kitten", "sitting") == 3
    assert calculate_edit_distance("saturday", "sunday") == 3

def test_case_sensitivity():
    """Test that the function is case-sensitive"""
    assert calculate_edit_distance("Hello", "hello") == 1

def test_unicode_strings():
    """Test edit distance with unicode strings"""
    assert calculate_edit_distance("café", "cafe") == 1

def test_type_error():
    """Test that type errors are raised for non-string inputs"""
    with pytest.raises(TypeError):
        calculate_edit_distance(123, "hello")
    
    with pytest.raises(TypeError):
        calculate_edit_distance("hello", [1, 2, 3])
    
    with pytest.raises(TypeError):
        calculate_edit_distance(None, "test")