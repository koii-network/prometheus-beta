import pytest
from src.find_minimum import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 7, 3, 15, 2]) == 2

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1]) == -1
    assert find_minimum([-5, -2, -10, -1]) == -10
    assert find_minimum([-3.5, 2.1, 0, -1]) == -3.5

def test_find_minimum_single_element():
    """Test finding minimum in a single-element array."""
    assert find_minimum([42]) == 42
    assert find_minimum([-42]) == -42

def test_find_minimum_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_find_minimum_non_numeric_array():
    """Test that a non-numeric array raises a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum([1, 2, 'a', 3])
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum(['hello', 'world'])