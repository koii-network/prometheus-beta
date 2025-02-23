import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test normal case with positive and negative numbers"""
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == [10, -4, 7]

def test_all_positive():
    """Test case with all positive numbers"""
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert max_subarray_sum(arr, k) == [4, 5]

def test_all_negative():
    """Test case with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == [-1, -2, -3]

def test_k_larger_than_list():
    """Test when k is larger than list length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) == []

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    k = 0
    assert max_subarray_sum(arr, k) == []

def test_empty_list():
    """Test with an empty list"""
    arr = []
    k = 2
    assert max_subarray_sum(arr, k) == []

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        max_subarray_sum(123, 2)
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], '2')

def test_negative_k():
    """Test negative k value"""
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], -1)

def test_single_element():
    """Test with single element"""
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == [5]