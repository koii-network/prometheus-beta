import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 6]) == 3

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1]) == -1
    assert find_minimum([-5, -3, -1]) == -5
    assert find_minimum([-10, 0, 10]) == -10

def test_find_minimum_float_numbers():
    """Test finding minimum in an array with floating-point numbers."""
    assert find_minimum([1.5, 2.3, 0.7]) == 0.7
    assert find_minimum([-1.5, 1.5, 0.0]) == -1.5

def test_find_minimum_single_element():
    """Test finding minimum in an array with a single element."""
    assert find_minimum([42]) == 42

def test_find_minimum_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_find_minimum_invalid_input():
    """Test that invalid input types raise appropriate exceptions."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(42)
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, 'a'])
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None])