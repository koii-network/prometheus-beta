import pytest
from src.max_subarray_sum import find_max_subarray_sum

def test_normal_positive_array():
    arr = [1, 2, 3, 4, 5]
    assert find_max_subarray_sum(arr) == [1, 2, 3, 4, 5]

def test_mixed_positive_negative():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert find_max_subarray_sum(arr) == [4, -1, 2, 1]

def test_all_negative():
    arr = [-1, -2, -3, -4, -5]
    assert find_max_subarray_sum(arr) == [-1]

def test_empty_array():
    arr = []
    assert find_max_subarray_sum(arr) == []

def test_single_element():
    arr = [42]
    assert find_max_subarray_sum(arr) == [42]

def test_multiple_max_sum_subarrays():
    # This test ensures that we return a valid max sum subarray 
    # when multiple subarrays have the same max sum
    arr = [1, -1, 2, 2, -1, 1]
    result = find_max_subarray_sum(arr)
    assert sum(result) == max_subarray_sum(arr)

def max_subarray_sum(arr):
    """
    Helper function to verify the sum of the max subarray
    """
    if not arr:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum