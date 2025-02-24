import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_case():
    """Test a basic scenario with a simple array."""
    arr = [1, 2, 3, 4]
    k = 10
    assert find_max_subarray_product_sum(arr, k) == 7  # [1, 2, 3]

def test_all_subarrays_valid():
    """Test when all subarrays are within the product constraint."""
    arr = [1, 2, 3, 4]
    k = 100
    assert find_max_subarray_product_sum(arr, k) == 10  # Full array sum

def test_no_valid_subarrays():
    """Test when no subarrays satisfy the product constraint."""
    arr = [5, 6, 7]
    k = 4
    assert find_max_subarray_product_sum(arr, k) == 0

def test_single_element_array():
    """Test with a single-element array."""
    arr = [3]
    k = 10
    assert find_max_subarray_product_sum(arr, k) == 3

def test_product_exact_match():
    """Test when a subarray's product is exactly the constraint."""
    arr = [1, 2, 3, 4]
    k = 6
    assert find_max_subarray_product_sum(arr, k) == 5  # [1, 2]

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)

def test_negative_integers_raises_error():
    """Test that negative integers raise a ValueError."""
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_product_sum([1, -2, 3], 10)

def test_zero_integers_raises_error():
    """Test that zero raises a ValueError."""
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_product_sum([1, 0, 3], 10)