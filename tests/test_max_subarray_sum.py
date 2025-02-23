import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    """Test basic functionality with a standard list"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == [10, 23, 3, 1]

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr, 0) == []

def test_k_larger_than_list():
    """Test when k is larger than the list length"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 5) == []

def test_k_equal_list_length():
    """Test when k is equal to the list length"""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr, 5) == [1, 2, 3, 4, 5]

def test_all_negative_numbers():
    """Test with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == [-1, -2, -3]

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    k = 4
    assert max_subarray_sum(arr, k) == [4, -1, 2, 1]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list", 3)
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], "not an int")

def test_negative_k():
    """Test error handling for negative k"""
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], -1)