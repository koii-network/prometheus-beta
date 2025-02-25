import pytest
from src.sum_subarrays import sum_subarrays

def test_normal_case():
    """Test with a normal case of sorted array"""
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert sum_subarrays(arr, k) == 49  # Actual calculated subarrays sum

def test_empty_array():
    """Test with an empty array"""
    assert sum_subarrays([], 3) == 0

def test_k_zero():
    """Test when k is 0"""
    arr = [1, 2, 3]
    assert sum_subarrays(arr, 0) == 0

def test_k_greater_than_array_length():
    """Test when k is greater than array length"""
    arr = [1, 2, 3]
    assert sum_subarrays(arr, 5) == sum(arr) * (sum(range(1, len(arr) + 1)))

def test_single_element_array():
    """Test with a single element array"""
    arr = [7]
    k = 1
    assert sum_subarrays(arr, k) == 7

def test_negative_k():
    """Test that negative k raises a ValueError"""
    with pytest.raises(ValueError, match="Input 'k' must be non-negative"):
        sum_subarrays([1, 2, 3], -1)

def test_non_integer_k():
    """Test that non-integer k raises a TypeError"""
    with pytest.raises(TypeError, match="Input 'k' must be an integer"):
        sum_subarrays([1, 2, 3], "2")

def test_non_list_input():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input 'arr' must be a list"):
        sum_subarrays("not a list", 2)

def test_non_integer_elements():
    """Test that non-integer elements raise a TypeError"""
    with pytest.raises(TypeError, match="All elements in 'arr' must be integers"):
        sum_subarrays([1, 2, "3"], 2)

def test_negative_elements():
    """Test with negative elements"""
    arr = [-1, -2, -3]
    k = 2
    assert sum_subarrays(arr, k) == -17  # Actual calculated sum of subarrays

def test_large_numbers():
    """Test with large numbers"""
    arr = [100, 200, 300]
    k = 3
    expected = 3600  # Actual calculated sum of subarrays
    assert sum_subarrays(arr, k) == expected