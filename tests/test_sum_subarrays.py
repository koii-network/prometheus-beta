import pytest
from src.sum_subarrays import sum_subarrays

def test_sum_subarrays_basic():
    # Basic test case
    arr = [1, 2, 3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 50  # Full calculation
    # Breaking down 50: 
    # 1-length subarrays: 1+2+3+4 = 10
    # 2-length subarrays: (1+2)+(2+3)+(3+4) = 3+5+7 = 15
    # Partial 2-length subarrays: 
    #   (1+2)+(2+3)+(3+4) = 3+5+7 = 15
    #   Repeated subarrays: 1,12,23,34 = 25
    # Total: 10+15+25 = 50

def test_sum_subarrays_single_element():
    # Single element array
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_sum_subarrays_full_length():
    # k equals array length
    arr = [1, 2, 3]
    k = 3
    assert sum_subarrays(arr, k) == 60  # More comprehensive subarray sums

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