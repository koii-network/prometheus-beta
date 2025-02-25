import pytest
from src.max_subarray_sum import find_max_subarray_sum

def test_standard_array():
    """Test with a standard mixed positive and negative array."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert find_max_subarray_sum(arr) == [4, -1, 2, 1]

def test_all_positive():
    """Test an array with all positive numbers."""
    arr = [1, 2, 3, 4, 5]
    assert find_max_subarray_sum(arr) == [1, 2, 3, 4, 5]

def test_all_negative():
    """Test an array with all negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    assert find_max_subarray_sum(arr) == [-1]

def test_single_element():
    """Test an array with a single element."""
    arr = [42]
    assert find_max_subarray_sum(arr) == [42]

def test_zero_sum_subarrays():
    """Test an array with multiple zero-sum subarrays."""
    arr = [1, -1, 2, -2, 3]
    assert 3 in find_max_subarray_sum(arr)

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_sum([])

def test_mixed_large_range():
    """Test an array with a mix of large positive and negative numbers."""
    arr = [10000, -5000, 6000, -2000, 15000]
    assert find_max_subarray_sum(arr) == [10000, -5000, 6000, -2000, 15000]

def test_repeated_max_sum():
    """Test an array with multiple subarrays having the same max sum."""
    arr = [1, 2, -1, 1, 2, -1]
    result = find_max_subarray_sum(arr)
    assert result in [[1, 2], [1, 2, -1, 1, 2]]