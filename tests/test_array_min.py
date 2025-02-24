import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([5, 2, 8, 1, 9]) == 1

def test_find_minimum_negative_numbers():
    """Test finding minimum in an array of negative numbers."""
    assert find_minimum([-5, -2, -8, -1, -9]) == -9

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-5, 2, 0, 8, -1]) == -5

def test_find_minimum_single_element():
    """Test finding minimum in an array with a single element."""
    assert find_minimum([42]) == 42

def test_find_minimum_floating_point():
    """Test finding minimum in an array with floating-point numbers."""
    assert find_minimum([3.14, 2.71, 1.41, 0.58]) == 0.58

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_non_numeric_array_raises_error():
    """Test that an array with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum([1, 2, 'a', 3])