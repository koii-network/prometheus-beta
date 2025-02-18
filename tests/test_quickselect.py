import pytest
from src.quickselect import quickselect

def test_quickselect_basic_cases():
    """Test basic functionality of quickselect."""
    assert quickselect([7, 10, 4, 3, 20, 15], 3) == 7
    assert quickselect([7, 10, 4, 3, 20, 15], 1) == 3
    assert quickselect([7, 10, 4, 3, 20, 15], 6) == 20

def test_quickselect_sorted_input():
    """Test quickselect with an already sorted input."""
    arr = [1, 2, 3, 4, 5]
    assert quickselect(arr, 3) == 3

def test_quickselect_reverse_sorted():
    """Test quickselect with a reverse sorted input."""
    arr = [5, 4, 3, 2, 1]
    assert quickselect(arr, 3) == 3

def test_quickselect_duplicate_elements():
    """Test quickselect with duplicate elements."""
    arr = [3, 3, 3, 3, 3]
    assert quickselect(arr, 3) == 3

def test_quickselect_single_element():
    """Test quickselect with a single element."""
    assert quickselect([42], 1) == 42

def test_quickselect_invalid_k_too_low():
    """Test that ValueError is raised when k is less than 1."""
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 0)

def test_quickselect_invalid_k_too_high():
    """Test that ValueError is raised when k is greater than array length."""
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 4)

def test_quickselect_empty_array():
    """Test that ValueError is raised for an empty array."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        quickselect([], 1)