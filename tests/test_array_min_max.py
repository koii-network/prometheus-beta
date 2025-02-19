import pytest
from src.array_min_max import find_min_max

def test_find_min_max_positive_numbers():
    """Test with an array of positive numbers"""
    result = find_min_max([1, 5, 3, 9, 2])
    assert result == (1, 9)

def test_find_min_max_mixed_numbers():
    """Test with an array of mixed positive and negative numbers"""
    result = find_min_max([-3, 0, 5, -1, 10])
    assert result == (-3, 10)

def test_find_min_max_single_element():
    """Test with an array containing a single element"""
    result = find_min_max([42])
    assert result == (42, 42)

def test_find_min_max_float_numbers():
    """Test with an array of floating point numbers"""
    result = find_min_max([1.5, 2.3, -0.7, 10.1])
    assert result == (-0.7, 10.1)

def test_find_min_max_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_min_max([])