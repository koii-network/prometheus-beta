import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    assert max_subarray_sum([42]) == 42

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_type_raises_error():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)