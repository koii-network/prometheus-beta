import pytest
from src.find_max import find_max

def test_find_max_positive_numbers():
    """Test finding max in a list of positive numbers."""
    assert find_max([1, 5, 3, 9, 2]) == 9

def test_find_max_negative_numbers():
    """Test finding max in a list of negative numbers."""
    assert find_max([-1, -5, -3, -9, -2]) == -1

def test_find_max_mixed_numbers():
    """Test finding max in a list with mixed positive and negative numbers."""
    assert find_max([-10, 0, 5, -3, 7]) == 7

def test_find_max_single_element():
    """Test finding max in a list with a single element."""
    assert find_max([42]) == 42

def test_find_max_floating_point():
    """Test finding max in a list with floating point numbers."""
    assert find_max([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_max([1, 2, "three", 4])