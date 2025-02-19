import pytest
from src.subarray_product_less_than_k import count_subarrays_with_product_less_than_k

def test_basic_case():
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 8

def test_no_valid_subarrays():
    nums = [1, 2, 3]
    k = 1
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array():
    nums = [5]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 1

def test_single_element_array_exceeding_k():
    nums = [10]
    k = 5
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_all_elements_less_than_k():
    nums = [1, 2, 3, 4]
    k = 20
    assert count_subarrays_with_product_less_than_k(nums, k) == 10

def test_large_k():
    nums = [1, 1, 1]
    k = 1000
    assert count_subarrays_with_product_less_than_k(nums, k) == 6

def test_mixed_values():
    nums = [2, 3, 4, 5]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 7