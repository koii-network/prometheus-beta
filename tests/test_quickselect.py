import pytest
from src.quickselect import quickselect

def test_quickselect_basic():
    """Test basic functionality of quickselect."""
    arr = [7, 10, 4, 3, 20, 15]
    assert quickselect(arr, 3) == 7  # 3rd smallest element
    assert quickselect(arr, 1) == 3  # smallest element
    assert quickselect(arr, 6) == 20  # largest element

def test_quickselect_sorted_array():
    """Test quickselect on a sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert quickselect(arr, 1) == 1
    assert quickselect(arr, 3) == 3
    assert quickselect(arr, 5) == 5

def test_quickselect_reverse_sorted():
    """Test quickselect on a reverse sorted array."""
    arr = [5, 4, 3, 2, 1]
    assert quickselect(arr, 1) == 1
    assert quickselect(arr, 3) == 3
    assert quickselect(arr, 5) == 5

def test_quickselect_with_duplicates():
    """Test quickselect with duplicate elements."""
    arr = [3, 3, 3, 3, 3]
    assert quickselect(arr, 1) == 3
    assert quickselect(arr, 3) == 3
    assert quickselect(arr, 5) == 3

def test_quickselect_error_cases():
    """Test error cases for quickselect."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        quickselect([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 4)

def test_quickselect_single_element():
    """Test quickselect with a single element array."""
    arr = [42]
    assert quickselect(arr, 1) == 42