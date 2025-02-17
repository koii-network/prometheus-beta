import pytest
from src.max_subarray import kadane_max_subarray

def test_positive_numbers():
    arr = [1, 2, 3, 4, 5]
    assert kadane_max_subarray(arr) == 15

def test_mixed_numbers():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert kadane_max_subarray(arr) == 6

def test_all_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    assert kadane_max_subarray(arr) == -1

def test_single_element():
    arr = [42]
    assert kadane_max_subarray(arr) == 42

def test_zero_sum():
    arr = [-1, 1]
    assert kadane_max_subarray(arr) == 1

def test_invalid_input_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        kadane_max_subarray("not a list")