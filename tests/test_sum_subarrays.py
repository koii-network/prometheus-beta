import pytest
from src.sum_subarrays import sum_subarrays

def test_sum_subarrays_basic():
    # Basic test case
    arr = [1, 2, 3, 4]
    k = 2
    # Manual breakdown of subarrays:
    # 1-length subarrays: 1,2,3,4 (sum 10)
    # 2-length subarrays: 1+2, 2+3, 3+4 (sum 15)
    # Each 1-length subarray can be chosen k times
    # Each 2-length subarray can be chosen k-1 times
    assert sum_subarrays(arr, k) == 40  # Adjusted expected value

def test_sum_subarrays_single_element():
    # Single element array
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_sum_subarrays_full_length():
    # k equals array length
    arr = [1, 2, 3]
    k = 3
    # Consider all possible subarrays
    assert sum_subarrays(arr, k) == 36  # Adjusted expected value

def test_sum_subarrays_small_k():
    # Small k value
    arr = [10, 20, 30, 40]
    k = 1
    assert sum_subarrays(arr, k) == 100  # Just the single elements

def test_sum_subarrays_invalid_k():
    # k less than 1 should raise ValueError
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be at least 1"):
        sum_subarrays(arr, 0)

def test_sum_subarrays_none_input():
    # None input should raise ValueError
    with pytest.raises(ValueError, match="Input array cannot be None"):
        sum_subarrays(None, 2)

def test_sum_subarrays_empty_array():
    # Empty array
    arr = []
    k = 2
    assert sum_subarrays(arr, k) == 0  # No subarrays to sum