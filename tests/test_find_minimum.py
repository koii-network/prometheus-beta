import pytest
from src.find_minimum import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 1]) == 1

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1, 2, 3]) == -1
    assert find_minimum([0, -5, 10, -3, 7]) == -5

def test_find_minimum_floating_point():
    """Test finding minimum in an array with floating-point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 3.7]) == 0.1
    assert find_minimum([-1.5, -2.3, -0.1, -3.7]) == -3.7

def test_minimum_single_element():
    """Test finding minimum in an array with a single element."""
    assert find_minimum([42]) == 42

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_non_numeric_array_raises_error():
    """Test that an array with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum([1, 2, 'a', 3])
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum([1, 2, None, 3])