import pytest
from src.max_subarray_product_sum import find_max_sum_subarray_with_product

def test_basic_scenario():
    """Test a basic scenario with a valid subarray."""
    arr = [1, 2, 3, 4]
    target_product = 6
    assert find_max_sum_subarray_with_product(arr, target_product) == 6  # 2 * 3

def test_multiple_subarrays():
    """Test when multiple subarrays exist with target product."""
    arr = [1, 2, 3, 2, 4]
    target_product = 6
    assert find_max_sum_subarray_with_product(arr, target_product) == 6  # 2 * 3

def test_no_matching_subarray():
    """Test when no subarray matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 100
    assert find_max_sum_subarray_with_product(arr, target_product) == -1

def test_single_element_matching():
    """Test when a single element matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 3
    assert find_max_sum_subarray_with_product(arr, target_product) == 3

def test_full_array_product():
    """Test when the entire array matches the target product."""
    arr = [1, 2, 3]
    target_product = 6
    assert find_max_sum_subarray_with_product(arr, target_product) == 6

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_sum_subarray_with_product([], 10)

def test_non_positive_integers_raises_error():
    """Test that an array with non-positive integers raises a ValueError."""
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_sum_subarray_with_product([1, 2, -3, 4], 10)
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_sum_subarray_with_product([0, 1, 2], 10)