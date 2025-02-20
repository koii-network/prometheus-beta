import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_normal_case():
    """Test with a standard case of positive and negative numbers."""
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == 16  # 10 + (-4) + 7

def test_max_subarray_sum_all_positive():
    """Test with all positive numbers."""
    arr = [2, 3, 4, 5, 6]
    k = 2
    assert max_subarray_sum(arr, k) == 11  # 5 + 6

def test_max_subarray_sum_all_negative():
    """Test with all negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3

def test_max_subarray_sum_single_element():
    """Test with single element case."""
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == 5

def test_max_subarray_sum_invalid_k_zero():
    """Test that a ValueError is raised when k is zero."""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_max_subarray_sum_invalid_k_large():
    """Test that a ValueError is raised when k is larger than array length."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 4)