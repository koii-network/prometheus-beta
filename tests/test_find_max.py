import pytest
from src.find_max import find_max_number

def test_find_max_basic():
    """Test finding max in a simple array of positive numbers"""
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_negative_numbers():
    """Test finding max in an array with negative numbers"""
    assert find_max_number([-1, -5, -3, -10]) == -1

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers"""
    assert find_max_number([-10, 0, 5, -3, 10]) == 10

def test_find_max_floats():
    """Test finding max in an array of floating point numbers"""
    assert find_max_number([1.5, 2.3, 0.1, 3.7]) == 3.7

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_non_numeric_array_raises_error():
    """Test that an array with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_max_number([1, 2, 'a', 3])