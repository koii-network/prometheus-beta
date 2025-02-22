import pytest
from src.subarray_product_sum import count_subarrays_product_less_than_k

def test_basic_scenarios():
    # Basic test cases
    assert count_subarrays_product_less_than_k([10, 5, 2, 6], 100) == 8
    assert count_subarrays_product_less_than_k([1, 2, 3], 0) == 0

def test_single_element_scenarios():
    # Single element scenarios
    assert count_subarrays_product_less_than_k([1], 1) == 0
    assert count_subarrays_product_less_than_k([2], 3) == 1
    assert count_subarrays_product_less_than_k([5], 5) == 0

def test_edge_cases():
    # Edge cases
    assert count_subarrays_product_less_than_k([], 10) == 0
    assert count_subarrays_product_less_than_k([10, 9, 10, 4, 3], 19) == 18

def test_large_numbers():
    # Large number of elements and large k
    large_nums = [1] * 30  # 30 ones
    assert count_subarrays_product_less_than_k(large_nums, 10) == 465

def test_all_small_numbers():
    # All small numbers
    assert count_subarrays_product_less_than_k([1, 1, 1], 2) == 6

def test_no_valid_subarrays():
    # No subarrays with product less than k
    assert count_subarrays_product_less_than_k([10, 20, 30], 5) == 0