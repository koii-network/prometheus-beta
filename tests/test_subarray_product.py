import pytest
from src.subarray_product import count_subarrays_with_product_less_than_k

def test_basic_cases():
    # Simple positive case
    assert count_subarrays_with_product_less_than_k([10, 5, 2, 6], 100) == 8
    
    # Empty array
    assert count_subarrays_with_product_less_than_k([], 10) == 0
    
    # k is 1
    assert count_subarrays_with_product_less_than_k([1, 2, 3], 1) == 0

def test_single_element_cases():
    # All numbers are less than k
    assert count_subarrays_with_product_less_than_k([1, 2, 3], 10) == 6
    
    # Some numbers less than k
    assert count_subarrays_with_product_less_than_k([1, 5, 2], 4) == 3

def test_edge_cases():
    # Large array
    nums = [1] * 10000
    assert count_subarrays_with_product_less_than_k(nums, 2) == 55005000
    
    # Exact k product
    assert count_subarrays_with_product_less_than_k([10, 5], 50) == 3

def test_error_cases():
    # k less than 1
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_with_product_less_than_k([1, 2, 3], 0)
    
    # Non-positive integers in array
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        count_subarrays_with_product_less_than_k([0, 1, 2], 10)
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        count_subarrays_with_product_less_than_k([-1, 2, 3], 10)