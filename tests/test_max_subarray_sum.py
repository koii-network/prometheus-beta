import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_and_negative_numbers():
    """Test with a mix of positive and negative numbers."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == 6  # Subarray [4, -1, 2, 1]

def test_all_positive_numbers():
    """Test when all numbers are positive."""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == 15  # Entire array

def test_all_negative_numbers():
    """Test when all numbers are negative."""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr) == -1  # Largest (least negative) number

def test_single_element():
    """Test with a single element."""
    arr = [42]
    assert max_subarray_sum(arr) == 42

def test_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([])

def test_alternating_signs():
    """Test array with alternating positive and negative numbers."""
    arr = [1, -1, 2, -2, 3, -3]
    assert max_subarray_sum(arr) == 3  # The last 3

def test_zero_sum_array():
    """Test an array that sums to zero."""
    arr = [-1, 1, -1, 1]
    assert max_subarray_sum(arr) == 1