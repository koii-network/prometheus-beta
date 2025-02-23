import pytest
from src.max_subarray import kadane_max_subarray

def test_basic_positive_numbers():
    """Test with a list of positive numbers."""
    assert kadane_max_subarray([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element():
    """Test with a single element list."""
    assert kadane_max_subarray([5]) == 5
    assert kadane_max_subarray([-5]) == -5

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert kadane_max_subarray([-1, -2, -3, -4]) == -1

def test_all_negative_single_max():
    """Test to ensure correct max is found in all negative numbers."""
    assert kadane_max_subarray([-5, -2, -1, -3]) == -1

def test_input_validation():
    """Test input validation."""
    # Empty list should raise ValueError
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])
    
    # Non-list input should raise TypeError
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        kadane_max_subarray("not a list")
        kadane_max_subarray(123)

def test_zero_sum_subarray():
    """Test with subarrays that sum to zero."""
    assert kadane_max_subarray([0, 0, 0, 0]) == 0
    assert kadane_max_subarray([-1, 1, -1, 1]) == 1

def test_large_numbers():
    """Test with large numbers."""
    assert kadane_max_subarray([10**6, -(10**6), 10**6]) == 10**6

def test_alternating_numbers():
    """Test with alternating positive and negative numbers."""
    assert kadane_max_subarray([1, -1, 2, -2, 3, -3]) == 3