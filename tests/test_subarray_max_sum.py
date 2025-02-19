import pytest
from src.subarray_max_sum import maxSumSubarray

def test_basic_max_sum_subarray():
    # Basic scenario with a simple array
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 3
    assert maxSumSubarray(arr, k) == 36  # 10 + 23 + 3 = 36

def test_single_element_arrays():
    # Test with single-element arrays
    arr = [5, 2, 8, 1, 9]
    k = 1
    assert maxSumSubarray(arr, k) == 9  # Maximum single-element is 9

def test_all_same_elements():
    # Test with all same elements
    arr = [7, 7, 7, 7, 7]
    k = 2
    assert maxSumSubarray(arr, k) == 14  # First two 7's

def test_negative_numbers():
    # Test with negative numbers
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert maxSumSubarray(arr, k) == -3  # -1 + -2 = -3

def test_edge_case_k_is_array_length():
    # Test when k is the entire array length
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert maxSumSubarray(arr, k) == 15  # Sum of entire array

def test_invalid_k_length_raises_error():
    # Test k larger than array
    arr = [1, 2, 3]
    k = 4
    with pytest.raises(ValueError, match="Subarray length cannot be larger than the array length"):
        maxSumSubarray(arr, k)

def test_non_positive_k_raises_error():
    # Test invalid k values
    arr = [1, 2, 3]
    invalid_k_values = [0, -1, -5]
    for k in invalid_k_values:
        with pytest.raises(ValueError, match="Subarray length must be a positive integer"):
            maxSumSubarray(arr, k)