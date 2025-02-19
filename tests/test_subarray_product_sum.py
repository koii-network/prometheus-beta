import pytest
from src.subarray_product_sum import count_subarrays_with_product_less_than_k

def test_basic_scenario():
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 29

def test_small_threshold():
    nums = [1, 2, 3, 4]
    k = 1
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array():
    nums = [3]
    k = 2
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array_valid():
    nums = [3]
    k = 5
    assert count_subarrays_with_product_less_than_k(nums, k) == 3

def test_empty_array():
    nums = []
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_all_elements_valid():
    nums = [1, 2, 3, 4]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 34

def test_negative_k():
    nums = [1, 2, 3]
    k = -1
    assert count_subarrays_with_product_less_than_k(nums, k) == 0