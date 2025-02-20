import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a normal case with positive and negative numbers"""
    arr = [1, -2, 3, 4, -1, 2, 1, 5, 4]
    k = 3
    assert max_subarray_sum(arr, k) == 10  # 4 + (-1) + 2 + 5

def test_all_positive():
    """Test case with all positive numbers"""
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert max_subarray_sum(arr, k) == 9  # 4 + 5

def test_all_negative():
    """Test case with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3

def test_single_element():
    """Test with k = 1"""
    arr = [5, 2, 7, 1, 9]
    k = 1
    assert max_subarray_sum(arr, k) == 9

def test_k_equals_array_length():
    """Test when k is equal to the array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_invalid_k_raises_value_error():
    """Test that invalid k values raise ValueError"""
    arr = [1, 2, 3, 4, 5]
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, -1)
    
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 6)

def test_empty_array():
    """Test empty array returns 0"""
    arr = []
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 1)