import pytest
from src.find_minimum import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([5, 2, 8, 1, 9]) == 1

def test_find_minimum_negative_numbers():
    """Test finding minimum in an array of negative numbers."""
    assert find_minimum([-5, -2, -8, -1, -9]) == -9

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-5, 2, 8, -1, 9]) == -5

def test_find_minimum_single_element():
    """Test finding minimum in an array with a single element."""
    assert find_minimum([42]) == 42

def test_find_minimum_floating_point():
    """Test finding minimum in an array of floating-point numbers."""
    assert find_minimum([3.14, 2.71, 1.41, 0.58]) == 0.58

def test_find_minimum_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])