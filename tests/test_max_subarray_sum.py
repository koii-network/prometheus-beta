import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    """Test with a basic array and k value"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_all_positive_numbers():
    """Test with an array of all positive numbers"""
    arr = [5, 2, 6, 8, 3, 1, 9]
    k = 3
    assert max_subarray_sum(arr, k) == 19  # 6 + 8 + 3 = 19

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, 4, -2, 10, -5, 3, 2]
    k = 3
    assert max_subarray_sum(arr, k) == 11  # 10 + -5 + 3 = 11

def test_minimum_length_k():
    """Test with k equal to array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15  # sum of entire array

def test_k_is_one():
    """Test with k = 1"""
    arr = [7, 2, 9, 1, 5]
    k = 1
    assert max_subarray_sum(arr, k) == 9  # max single element

def test_invalid_k_raises_error():
    """Test that invalid k values raise ValueError"""
    arr = [1, 2, 3, 4]
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)
    
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 5)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 1)