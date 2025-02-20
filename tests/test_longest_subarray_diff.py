import pytest
from src.longest_subarray_diff import find_longest_subarray_with_diff

def test_basic_scenarios():
    # Basic scenarios
    assert find_longest_subarray_with_diff([1, 2, 3, 4], 1) == 4  # All adjacent differences >= 1
    assert find_longest_subarray_with_diff([1, 3, 6, 10], 3) == 3  # Subarray of length 3
    assert find_longest_subarray_with_diff([1, 1, 1, 1], 2) == 1  # No adjacent differences meet condition

def test_single_element_array():
    # Single element array should always return 1
    assert find_longest_subarray_with_diff([5], 0) == 1
    assert find_longest_subarray_with_diff([5], 1) == 1

def test_two_element_arrays():
    # Two element arrays
    assert find_longest_subarray_with_diff([1, 5], 3) == 2  # Difference meets condition
    assert find_longest_subarray_with_diff([1, 2], 2) == 1  # Difference does not meet condition

def test_non_consecutive_subarray():
    # Array where maximum subarray is not consecutive
    assert find_longest_subarray_with_diff([1, 5, 3, 8, 2], 3) == 3

def test_error_handling():
    # Error handling tests
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_longest_subarray_with_diff([], 1)
    
    with pytest.raises(ValueError, match="Difference k must be non-negative"):
        find_longest_subarray_with_diff([1, 2, 3], -1)

def test_large_arrays():
    # Larger array test
    arr = list(range(1, 101))  # 1 to 100
    assert find_longest_subarray_with_diff(arr, 1) == 100  # Each adjacent element differs by 1

def test_random_arrays():
    # More complex array scenarios
    assert find_longest_subarray_with_diff([10, 1, 6, 3, 8], 4) == 3
    assert find_longest_subarray_with_diff([7, 2, 10, 5, 3, 9], 5) == 3