import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_array():
    # Basic test case
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_arrays():
    # Test with k=1
    arr = [5, 2, 8, 1, 9]
    k = 1
    assert max_subarray_sum(arr, k) == 9

def test_full_array_sum():
    # When k equals array length
    arr = [3, 7, 2, 1]
    k = 4
    assert max_subarray_sum(arr, k) == 13

def test_negative_numbers():
    # Array with negative numbers
    arr = [-1, -2, 3, 4, -5, 6, 7]
    k = 3
    assert max_subarray_sum(arr, k) == 14  # 3 + 4 + (-5)

def test_invalid_k_raises_error():
    # Test error handling
    arr = [1, 2, 3, 4, 5]
    
    # k larger than array length
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 6)
    
    # k is zero or negative
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, -2)

def test_all_same_elements():
    # Array with all same elements
    arr = [5, 5, 5, 5, 5]
    k = 3
    assert max_subarray_sum(arr, k) == 15