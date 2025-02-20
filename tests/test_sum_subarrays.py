import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_functionality():
    """Test basic summing of subarrays"""
    arr = [1, 2, 3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 50  # Calculated subarrays: [1], [1,2], [2], [2,3], [3], [3,4], [4]

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3, 4]
    k = 0
    assert sum_subarrays(arr, k) == 0

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 5
    assert sum_subarrays(arr, k) == 50

def test_negative_k_raises_error():
    """Test that negative k raises a ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a non-negative integer"):
        sum_subarrays(arr, -1)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    k = 3
    assert sum_subarrays(arr, k) == 0

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input arr must be a list"):
        sum_subarrays("not a list", 2)
    
    with pytest.raises(TypeError, match="Input k must be an integer"):
        sum_subarrays([1, 2, 3], "not an int")