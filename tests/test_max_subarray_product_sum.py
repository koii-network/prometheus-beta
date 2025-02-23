import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_case():
    """Test with a simple scenario where a subarray exists"""
    arr = [1, 2, 3, 4, 5]
    target_product = 24
    assert find_max_subarray_product_sum(arr, target_product) == 12  # [3, 4] or [4, 3]

def test_multiple_valid_subarrays():
    """Test a case with multiple subarrays matching the product"""
    arr = [2, 3, 4, 5, 6]
    target_product = 24
    assert find_max_subarray_product_sum(arr, target_product) == 15  # [3, 4, 5]

def test_single_element_match():
    """Test when a single element matches the product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 4
    assert find_max_subarray_product_sum(arr, target_product) == 4

def test_no_matching_subarray():
    """Test when no subarray matches the target product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 1000
    assert find_max_subarray_product_sum(arr, target_product) is None

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)

def test_negative_integers_raises_error():
    """Test that an array with non-positive integers raises a ValueError"""
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_product_sum([1, 2, -3, 4], 10)

def test_first_matching_subarray():
    """Test the first matching subarray when multiple exist"""
    arr = [2, 3, 2, 4]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 5  # [2, 3]