import pytest
from src.quickselect import quickselect

def test_quickselect_basic():
    """Test basic functionality of quickselect"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert quickselect(arr, 1) == 1  # Smallest element
    assert quickselect(arr, 6) == 4  # 6th smallest element
    assert quickselect(arr, len(arr)) == 9  # Largest element

def test_quickselect_sorted_array():
    """Test quickselect on a sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert quickselect(arr, 3) == 3

def test_quickselect_reverse_sorted_array():
    """Test quickselect on a reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    assert quickselect(arr, 3) == 3

def test_quickselect_duplicate_elements():
    """Test quickselect with duplicate elements"""
    arr = [3, 3, 3, 3, 3]
    assert quickselect(arr, 3) == 3

def test_quickselect_single_element():
    """Test quickselect with a single element"""
    arr = [42]
    assert quickselect(arr, 1) == 42

def test_quickselect_invalid_k_lower_bound():
    """Test quickselect with k less than 1"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        quickselect(arr, 0)

def test_quickselect_invalid_k_upper_bound():
    """Test quickselect with k greater than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        quickselect(arr, 4)

def test_quickselect_empty_array():
    """Test quickselect with an empty array"""
    arr = []
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        quickselect(arr, 1)

def test_quickselect_negative_numbers():
    """Test quickselect with negative numbers"""
    arr = [-5, -3, -1, -8, -2, -4]
    assert quickselect(arr, 2) == -4  # 2nd smallest element