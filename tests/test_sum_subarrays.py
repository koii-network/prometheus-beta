import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_sum_subarrays():
    # Basic test with a simple sorted array
    arr = [1, 2, 3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 50  # Calculated manually

def test_single_element_array():
    # Test with a single element array
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_full_array_sum():
    # Test with k equal to array length
    arr = [1, 2, 3]
    k = 3
    assert sum_subarrays(arr, k) == 60  # Sum of all possible subarrays

def test_k_less_than_array_length():
    # Test with k less than array length
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert sum_subarrays(arr, k) == 120  # Sum of subarrays up to length 2

def test_invalid_k_raises_error():
    # Test that k < 1 raises a ValueError
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be at least 1"):
        sum_subarrays(arr, 0)

def test_none_array_raises_error():
    # Test that None array raises a ValueError
    with pytest.raises(ValueError, match="Input array cannot be None"):
        sum_subarrays(None, 2)

def test_empty_array():
    # Test with an empty array
    arr = []
    k = 1
    assert sum_subarrays(arr, k) == 0