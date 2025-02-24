import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in a list of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 7]) == 3

def test_find_minimum_negative_numbers():
    """Test finding minimum in a list of negative numbers."""
    assert find_minimum([-1, -2, -3, -4, -5]) == -5
    assert find_minimum([-5, -4, -3, -2, -1]) == -5

def test_find_minimum_mixed_numbers():
    """Test finding minimum in a list with mixed positive and negative numbers."""
    assert find_minimum([-10, 0, 10, 5, -5]) == -10
    assert find_minimum([0, -1, 1]) == -1

def test_find_minimum_floating_point():
    """Test finding minimum with floating point numbers."""
    assert find_minimum([1.5, 2.5, 0.5, 3.5]) == 0.5

def test_find_minimum_error_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty list"):
        find_minimum([])

def test_find_minimum_error_non_list():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(123)

def test_find_minimum_error_non_numeric():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None])