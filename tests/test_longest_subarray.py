import pytest
from src.longest_subarray import find_longest_subarray

def test_basic_functionality():
    # Basic test case
    assert find_longest_subarray([1, 5, 3, 8, 7], 2) == 3

def test_single_element():
    # Single element array
    assert find_longest_subarray([5], 1) == 1

def test_all_differences_meet_condition():
    # All adjacent differences meet the condition
    assert find_longest_subarray([1, 4, 8, 13], 3) == 4

def test_intermittent_valid_differences():
    # Intermittent valid differences
    assert find_longest_subarray([1, 2, 5, 3, 7, 8, 9], 3) == 3

def test_k_zero():
    # When k is zero
    assert find_longest_subarray([1, 1, 2, 2, 3, 3], 0) == 2

def test_empty_array_raises_error():
    # Empty array should raise ValueError
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_longest_subarray([], 2)

def test_negative_k_raises_error():
    # Negative k should raise ValueError
    with pytest.raises(ValueError, match="k must be non-negative"):
        find_longest_subarray([1, 2, 3], -1)

def test_no_valid_subarray():
    # No subarray meets the condition
    assert find_longest_subarray([1, 2, 3, 4, 5], 10) == 1

def test_large_differences():
    # Large differences
    assert find_longest_subarray([10, 20, 50, 100, 200], 30) == 4