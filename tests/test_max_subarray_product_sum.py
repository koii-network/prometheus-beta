import pytest
from src.max_subarray_product_sum import find_max_subarray_sum_with_product

def test_basic_scenario():
    arr = [1, 2, 3, 4]
    target_product = 6
    assert find_max_subarray_sum_with_product(arr, target_product) == 5  # Subarray [2, 3]

def test_multiple_valid_subarrays():
    arr = [1, 2, 3, 2, 4]
    target_product = 6
    assert find_max_subarray_sum_with_product(arr, target_product) == 9  # Subarray [2, 3, 2, 2]

def test_single_element_match():
    arr = [1, 2, 3, 4, 5]
    target_product = 3
    assert find_max_subarray_sum_with_product(arr, target_product) == 3  # Subarray [3]

def test_no_matching_subarray():
    arr = [1, 2, 3, 4, 5]
    target_product = 100
    assert find_max_subarray_sum_with_product(arr, target_product) == 0

def test_raises_error_for_empty_array():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_sum_with_product([], 10)

def test_raises_error_for_non_positive_integers():
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_sum_with_product([1, 2, -3, 4], 10)

def test_large_product_scenario():
    arr = [10, 2, 3, 4, 5]
    target_product = 120
    assert find_max_subarray_sum_with_product(arr, target_product) == 24  # Subarray [3, 4, 5]