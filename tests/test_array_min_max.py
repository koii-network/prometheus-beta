import pytest
from src.array_min_max import find_min_max

def test_find_min_max_basic():
    """Test basic functionality with positive and negative numbers."""
    assert find_min_max([1, 2, 3, 4, 5]) == (1, 5)
    assert find_min_max([-1, 0, 1]) == (-1, 1)

def test_find_min_max_floats():
    """Test with floating-point numbers."""
    assert find_min_max([1.5, 2.7, -3.2, 0.1]) == (-3.2, 2.7)

def test_find_min_max_large_numbers():
    """Test with large numbers."""
    assert find_min_max([10**6, -10**6, 0]) == (-10**6, 10**6)

def test_find_min_max_single_element():
    """Test with a single-element list."""
    assert find_min_max([42]) == (42, 42)

def test_find_min_max_empty_list_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_min_max([])

def test_find_min_max_non_list_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min_max("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min_max(123)

def test_find_min_max_non_numeric_error():
    """Test that lists with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_min_max([1, 2, "three"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_min_max([1, 2, None])