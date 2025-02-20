import pytest
from src.longest_subarray import longest_subarray_k_diff

def test_basic_scenarios():
    # Basic scenarios
    assert longest_subarray_k_diff([1, 5, 3, 8, 12], 3) == 3  # [3, 8, 12]
    assert longest_subarray_k_diff([1, 2, 3, 4], 1) == 4  # Entire array
    assert longest_subarray_k_diff([1, 1, 1, 1], 2) == 1  # No valid subarray longer than 1

def test_single_element():
    # Single element array always returns 1
    assert longest_subarray_k_diff([5], 0) == 1
    assert longest_subarray_k_diff([5], 1) == 1

def test_edge_cases():
    # Edge cases
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        longest_subarray_k_diff([], 1)
    
    with pytest.raises(ValueError, match="k must be non-negative"):
        longest_subarray_k_diff([1, 2, 3], -1)

def test_various_scenarios():
    # Various input scenarios
    assert longest_subarray_k_diff([10, 5, 8, 12, 20], 4) == 3  # [5, 8, 12]
    assert longest_subarray_k_diff([7, 1, 5, 10, 15], 5) == 3  # [1, 5, 10]
    assert longest_subarray_k_diff([2, 4, 6, 8, 10], 2) == 5  # Entire array