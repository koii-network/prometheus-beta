import pytest
from src.array_min_max import find_min_max

def test_find_min_max_basic():
    """Test basic functionality with a list of integers."""
    assert find_min_max([1, 2, 3, 4, 5]) == (1, 5)

def test_find_min_max_with_negative_numbers():
    """Test functionality with negative numbers."""
    assert find_min_max([-1, -2, 0, 2, 1]) == (-2, 2)

def test_find_min_max_with_floats():
    """Test functionality with floating point numbers."""
    assert find_min_max([1.5, -2.5, 0.0, 3.7]) == (-2.5, 3.7)

def test_find_min_max_mixed_numbers():
    """Test functionality with mixed integer and float numbers."""
    assert find_min_max([1, -5, 3.14, 0, -2.5]) == (-5, 3.14)

def test_find_min_max_single_element():
    """Test with a single element list."""
    assert find_min_max([42]) == (42, 42)

def test_find_min_max_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_min_max([])

def test_find_min_max_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min_max("not a list")

def test_find_min_max_non_numeric_input_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_min_max([1, 2, "three", 4])