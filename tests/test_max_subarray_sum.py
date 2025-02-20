import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_array():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    assert max_subarray_sum([42]) == 42

def test_alternating_elements():
    assert max_subarray_sum([-1, 1, -1, 1, -1]) == 1

def test_mixed_elements():
    assert max_subarray_sum([-2, 5, -1, 3, -3, 2, 4]) == 13

def test_input_type_error():
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list_error():
    with pytest.raises(ValueError):
        max_subarray_sum([])