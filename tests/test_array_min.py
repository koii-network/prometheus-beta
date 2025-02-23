import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 7]) == 3

def test_find_minimum_mixed_numbers():
    """Test finding minimum in array with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1]) == -1
    assert find_minimum([-5, -2, -10, -1]) == -10
    assert find_minimum([-3, 0, 3]) == -3

def test_find_minimum_floating_point():
    """Test finding minimum in array with floating-point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 4.7]) == 0.1
    assert find_minimum([-1.5, -2.3, -0.1, -4.7]) == -4.7

def test_find_minimum_single_element():
    """Test finding minimum in single-element array."""
    assert find_minimum([42]) == 42

def test_find_minimum_empty_array():
    """Test that finding minimum in empty array raises ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_find_minimum_invalid_input():
    """Test that invalid input types raise appropriate exceptions."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(123)
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, 'a', 3])
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None, 3])