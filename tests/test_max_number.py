import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_numbers():
    """Test finding max in an array of positive numbers"""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 12, 3]) == 12

def test_find_max_number_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers"""
    assert find_max_number([-1, 0, 5, -10, 3]) == 5
    assert find_max_number([-5, -2, -10, -1]) == -1

def test_find_max_number_single_element():
    """Test finding max in an array with a single element"""
    assert find_max_number([42]) == 42

def test_find_max_number_floating_point():
    """Test finding max in an array with floating point numbers"""
    assert find_max_number([1.5, 2.7, 0.3, 3.14]) == 3.14

def test_find_max_number_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])