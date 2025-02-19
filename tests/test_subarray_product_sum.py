import pytest
from src.subarray_product_sum import count_subarrays_with_product_less_than_k

def test_basic_case():
    """Test a basic scenario with multiple subarrays"""
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 8

def test_empty_array():
    """Test with an empty array"""
    nums = []
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array():
    """Test with a single element array"""
    nums = [3]
    k = 3
    assert count_subarrays_with_product_less_than_k(nums, k) == 1
    
    nums = [5]
    k = 3
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_no_valid_subarrays():
    """Test when no subarrays have product less than k"""
    nums = [10, 20, 30]
    k = 5
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_all_subarrays_valid():
    """Test when all subarrays are valid"""
    nums = [1, 1, 1]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 6

def test_invalid_k():
    """Test handling of invalid k value"""
    nums = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be at least 1"):
        count_subarrays_with_product_less_than_k(nums, 0)

def test_large_k():
    """Test with a very large k"""
    nums = [1000, 1000, 1000]
    k = 1000000
    assert count_subarrays_with_product_less_than_k(nums, k) == 6