import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_case():
    """Test a basic scenario with a simple array."""
    arr = [1, 2, 3, 4, 5]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 5

def test_multiple_valid_subarrays():
    """Test when multiple subarrays have the target product."""
    arr = [1, 2, 3, 2, 4, 3]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 9

def test_single_element_array():
    """Test an array with a single element."""
    arr = [6]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 6

def test_no_matching_subarray():
    """Test when no subarray matches the target product."""
    arr = [1, 2, 3, 4, 5]
    target_product = 100
    assert find_max_subarray_product_sum(arr, target_product) == -1

def test_large_array():
    """Test with a larger array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_product = 24
    assert find_max_subarray_product_sum(arr, target_product) == 20

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)
    
    with pytest.raises(ValueError, match="All integers must be positive"):
        find_max_subarray_product_sum([1, 2, -3, 4], 10)
    
    with pytest.raises(ValueError, match="All integers must be positive"):
        find_max_subarray_product_sum([0, 1, 2, 3], 10)