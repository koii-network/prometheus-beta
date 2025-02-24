import pytest
from src.find_max import find_max

def test_find_max_positive_numbers():
    """Test finding max in an array of positive numbers."""
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_negative_numbers():
    """Test finding max in an array of negative numbers."""
    assert find_max([-5, -3, -10, -1]) == -1

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers."""
    assert find_max([-5, 0, 10, -3, 7]) == 10

def test_find_max_single_element():
    """Test finding max in an array with a single element."""
    assert find_max([42]) == 42

def test_find_max_floats():
    """Test finding max in an array of floating point numbers."""
    assert find_max([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max("not a list")

def test_non_numeric_input_raises_error():
    """Test that an array with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max([1, 2, "three", 4])

def test_mixed_numeric_types():
    """Test finding max with a mix of integers and floats."""
    assert find_max([1, 2.5, 3, 4.7, 2]) == 4.7