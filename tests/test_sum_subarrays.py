import pytest
from src.sum_subarrays import sum_subarrays

def test_sum_subarrays_basic():
    # Test with a simple sorted array
    arr = [1, 2, 3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 50  # Detailed calculation explained below

def test_sum_subarrays_empty():
    # Test with an empty array
    assert sum_subarrays([], 3) == 0

def test_sum_subarrays_zero_k():
    # Test with k = 0
    arr = [1, 2, 3]
    assert sum_subarrays(arr, 0) == 0

def test_sum_subarrays_k_greater_than_length():
    # Test when k is larger than array length
    arr = [1, 2, 3]
    assert sum_subarrays(arr, 5) == 50  # Full combinatorial sum

def test_sum_subarrays_single_element():
    # Test with a single element array
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_sum_subarrays_negative_numbers():
    # Test with negative numbers in the array
    arr = [-1, 2, -3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 14  # Sum of all subarrays <=2 length

# Detailed explanation of the first test case calculation
# For arr = [1, 2, 3, 4] and k = 2, subarrays (with their sums):
# [1] = 1
# [2] = 2
# [3] = 3
# [4] = 4
# [1,2] = 3
# [2,3] = 5
# [3,4] = 7
# [1,2,3] = 6
# Total sum = 1 + 2 + 3 + 4 + 3 + 5 + 7 + 6 = 50