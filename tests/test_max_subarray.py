import pytest
from src.max_subarray import find_max_subarray

def test_basic_positive_array():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert find_max_subarray(arr) == [4, -1, 2, 1]

def test_all_positive_array():
    arr = [1, 2, 3, 4, 5]
    assert find_max_subarray(arr) == [1, 2, 3, 4, 5]

def test_all_negative_array():
    arr = [-1, -2, -3, -4, -5]
    assert find_max_subarray(arr) == [-1]

def test_single_element_array():
    arr = [42]
    assert find_max_subarray(arr) == [42]

def test_empty_array():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray([])

def test_zero_sum_array():
    arr = [-1, 1, 0, -1, 1]
    result = find_max_subarray(arr)
    assert result == [1] or result == [-1, 1] or result == [1, 0, -1, 1]