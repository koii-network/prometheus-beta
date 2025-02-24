import pytest
from src.find_minimum import find_minimum

def test_find_minimum_basic():
    """Test finding minimum in a standard numeric array."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([-1, 0, 1]) == -1

def test_find_minimum_with_floats():
    """Test finding minimum with floating point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 3.7]) == 0.1
    assert find_minimum([-1.5, -0.5, 0.5]) == -1.5

def test_find_minimum_single_element():
    """Test finding minimum with a single-element array."""
    assert find_minimum([42]) == 42

def test_find_minimum_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_find_minimum_non_numeric():
    """Test that non-numeric arrays raise a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum(['a', 'b', 'c'])
    
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_minimum([1, 2, 'three'])

def test_find_minimum_mixed_positive_negative():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-10, 0, 10, -5, 5]) == -10