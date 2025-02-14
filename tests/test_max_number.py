import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_integers():
    """Test finding max in an array of positive integers"""
    assert find_max_number([1, 5, 3, 9, 2]) == 9

def test_find_max_number_negative_integers():
    """Test finding max in an array with negative integers"""
    assert find_max_number([-1, -5, -3, -9, -2]) == -1

def test_find_max_number_mixed_integers():
    """Test finding max in an array with mixed positive and negative integers"""
    assert find_max_number([-10, 0, 5, 3, -7]) == 5

def test_find_max_number_floats():
    """Test finding max in an array of floats"""
    assert find_max_number([1.5, 3.7, 2.1, 4.2]) == 4.2

def test_find_max_number_single_element():
    """Test finding max in an array with a single element"""
    assert find_max_number([42]) == 42

def test_find_max_number_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_find_max_number_non_list_raises_error():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")

def test_find_max_number_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, "three", 4])