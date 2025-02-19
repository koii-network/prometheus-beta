import pytest
from src.median_finder import find_median_index

def test_median_index_odd_length():
    """Test median index for odd-length sorted array"""
    arr = [1, 3, 5, 7, 9]
    assert find_median_index(arr) == 2  # index 2 (value 5)

def test_median_index_even_length():
    """Test median index for even-length sorted array"""
    arr = [1, 2, 3, 4]
    assert find_median_index(arr) == 2.5  # average of 2 and 3

def test_single_element_array():
    """Test array with a single element"""
    arr = [42]
    assert find_median_index(arr) == 0  # only index is 0

def test_two_element_array():
    """Test array with two elements"""
    arr = [1, 2]
    assert find_median_index(arr) == 1.5  # average of 1 and 2

def test_empty_array():
    """Test empty array raises ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_median_index([])