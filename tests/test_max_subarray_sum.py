import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_max_subarray_sum_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([42]) == 42

def test_max_subarray_sum_large_numbers():
    assert max_subarray_sum([10000, -5000, 20000, -15000]) == 25000

def test_max_subarray_sum_invalid_input_type():
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_max_subarray_sum_empty_list():
    with pytest.raises(ValueError):
        max_subarray_sum([])