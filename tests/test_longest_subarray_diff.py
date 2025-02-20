import pytest
from src.longest_subarray_diff import longest_subarray_with_diff

def test_basic_scenarios():
    # Test case with standard input
    assert longest_subarray_with_diff([1, 5, 3, 8, 6], 2) == 4
    
    # Test case where entire array satisfies condition
    assert longest_subarray_with_diff([1, 3, 5, 7, 9], 2) == 5
    
    # Test case with no valid subarray
    assert longest_subarray_with_diff([1, 2, 3, 4], 5) == 1

def test_edge_cases():
    # Empty list
    assert longest_subarray_with_diff([], 2) == 0
    
    # Single element list
    assert longest_subarray_with_diff([5], 1) == 1

def test_error_cases():
    # Invalid input type for A
    with pytest.raises(ValueError, match="Input must be a list"):
        longest_subarray_with_diff("not a list", 2)
    
    # Invalid input type for k
    with pytest.raises(ValueError, match="k must be an integer"):
        longest_subarray_with_diff([1, 2, 3], "not an int")

def test_complex_scenarios():
    # Multiple segments, finding the longest
    assert longest_subarray_with_diff([10, 1, 5, 3, 8, 6, 2, 9], 3) == 3
    
    # Negative numbers
    assert longest_subarray_with_diff([-1, -5, -3, -8, -6], 2) == 4

def test_zero_difference():
    # Zero as the minimum difference allowed
    assert longest_subarray_with_diff([1, 1, 1, 2, 2, 3], 0) == 6