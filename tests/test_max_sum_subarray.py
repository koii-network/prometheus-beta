import pytest
from src.max_sum_subarray import maxSumSubarray

def test_basic_max_sum_subarray():
    # Basic scenario with multiple subarrays
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert maxSumSubarray(arr, k) == 39  # max sum from [10, 23, 3, 1] or [23, 3, 1, 0]

def test_single_subarray():
    # Scenario with only one possible subarray
    arr = [5, 6, 7, 8]
    k = 4
    assert maxSumSubarray(arr, k) == 26

def test_large_values():
    # Test with large numbers
    arr = [100, 200, 300, 400, 500]
    k = 3
    assert maxSumSubarray(arr, k) == 1200

def test_mixed_values():
    # Test with mixed positive and negative numbers
    arr = [-1, 5, -3, 10, -2, 8, 6]
    k = 3
    assert maxSumSubarray(arr, k) == 14

def test_invalid_k_zero():
    # Test with k = 0
    arr = [1, 2, 3, 4]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray(arr, 0)

def test_invalid_k_too_large():
    # Test with k larger than array length
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        maxSumSubarray(arr, 4)

def test_single_element_array():
    # Test with single element array and k=1
    arr = [42]
    assert maxSumSubarray(arr, 1) == 42

def test_empty_array():
    # Test with empty array (will raise an error)
    arr = []
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        maxSumSubarray(arr, 1)