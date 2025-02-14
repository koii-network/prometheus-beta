import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_integers():
    """Test finding max in an array of positive integers."""
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_number_mixed_integers():
    """Test finding max in an array with mixed positive and negative integers."""
    assert find_max_number([-10, 0, 5, -3, 7]) == 7

def test_find_max_number_floating_point():
    """Test finding max in an array with floating-point numbers."""
    assert find_max_number([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_find_max_number_single_element():
    """Test finding max in an array with a single element."""
    assert find_max_number([42]) == 42

def test_find_max_number_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_find_max_number_non_numeric():
    """Test that an array with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_max_number([1, 2, '3', 4])

def test_find_max_number_mixed_numeric_types():
    """Test finding max in an array with mixed integer and float types."""
    assert find_max_number([1, 2.5, 3, 4.7]) == 4.7