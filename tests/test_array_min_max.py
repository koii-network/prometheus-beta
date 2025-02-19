import pytest
from src.array_min_max import find_min_max

def test_find_min_max_basic():
    """Test finding min and max in a standard numeric array."""
    result = find_min_max([1, 2, 3, 4, 5])
    assert result == (1, 5)

def test_find_min_max_negative_numbers():
    """Test finding min and max with negative numbers."""
    result = find_min_max([-10, 0, 10, -5, 5])
    assert result == (-10, 10)

def test_find_min_max_duplicates():
    """Test an array with duplicate values."""
    result = find_min_max([5, 5, 5, 5])
    assert result == (5, 5)

def test_find_min_max_single_element():
    """Test an array with a single element."""
    result = find_min_max([42])
    assert result == (42, 42)

def test_find_min_max_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_min_max([])

def test_find_min_max_non_numeric():
    """Test that non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_min_max([1, 2, "three", 4, 5])