import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a normal case with multiple elements"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test an array with only one element"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_all_same_elements():
    """Test an array with all same elements"""
    arr = [2, 2, 2, 2, 2]
    assert max_subarray_sum(arr, 3) == 6

def test_negative_numbers():
    """Test an array with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3 = -6

def test_invalid_k_too_large():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k cannot be greater than array length"):
        max_subarray_sum(arr, 4)

def test_invalid_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_invalid_k_negative():
    """Test when k is negative"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum(arr, -1)

def test_empty_array():
    """Test an empty array"""
    arr = []
    with pytest.raises(ValueError, match="Subarray length k cannot be greater than array length"):
        max_subarray_sum(arr, 1)