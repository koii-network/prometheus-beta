import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_normal_case():
    """Test the function with a normal input array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    result = max_subarray_sum(arr, k)
    assert result == 39  # 10 + 23 + 3 + 1 = 39

def test_max_subarray_sum_all_positive():
    """Test with an array of all positive numbers"""
    arr = [5, 7, 8, 9, 10]
    k = 3
    result = max_subarray_sum(arr, k)
    assert result == 27  # 8 + 9 + 10 = 27

def test_max_subarray_sum_mixed_numbers():
    """Test with an array containing positive and negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    k = 3
    result = max_subarray_sum(arr, k)
    assert result == 5  # 4 + (-1) + 2 = 5

def test_max_subarray_sum_single_element_arrays():
    """Test with small arrays where k equals array length"""
    arr = [42]
    k = 1
    result = max_subarray_sum(arr, k)
    assert result == 42

def test_max_subarray_sum_zero_elements():
    """Test raising ValueError when k is zero"""
    arr = [1, 2, 3, 4, 5]
    k = 0
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, k)

def test_max_subarray_sum_k_larger_than_array():
    """Test raising ValueError when k is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, k)

def test_max_subarray_sum_negative_k():
    """Test raising ValueError when k is negative"""
    arr = [1, 2, 3, 4, 5]
    k = -2
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, k)