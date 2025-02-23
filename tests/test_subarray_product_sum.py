import pytest
from src.subarray_product_sum import count_subarrays_with_product_less_than_k

def test_basic_functionality():
    """Test basic functionality with a simple array."""
    assert count_subarrays_with_product_less_than_k([10, 5, 2, 6], 100) == 8

def test_empty_array():
    """Test with an empty array."""
    assert count_subarrays_with_product_less_than_k([], 10) == 0

def test_no_valid_subarrays():
    """Test when no subarrays meet the condition."""
    assert count_subarrays_with_product_less_than_k([10, 20, 30], 5) == 0

def test_single_element_array():
    """Test with a single element array."""
    assert count_subarrays_with_product_less_than_k([3], 5) == 1
    assert count_subarrays_with_product_less_than_k([10], 5) == 0

def test_all_elements_valid():
    """Test when all elements are less than k."""
    assert count_subarrays_with_product_less_than_k([1, 2, 3, 4], 20) == 8

def test_some_elements_valid():
    """Test when some elements are valid."""
    assert count_subarrays_with_product_less_than_k([1, 1, 1], 2) == 6

def test_invalid_input_type():
    """Test with invalid input types."""
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k("not a list", 10)
    
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k([1, 2, 3], "not a number")

def test_invalid_k_value():
    """Test with invalid k values."""
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k([1, 2, 3], 0)
    
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k([1, 2, 3], -5)