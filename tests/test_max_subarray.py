import pytest
from src.max_subarray import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15
    assert max_subarray_sum([5, -2, 3, 4, -1, 2, 1]) == 12

def test_max_subarray_sum_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1, -1, 1, -1, 1]) == 1

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([42]) == 42
    assert max_subarray_sum([-42]) == -42

def test_max_subarray_sum_error_handling():
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    
    with pytest.raises(TypeError):
        max_subarray_sum(123)
    
    with pytest.raises(ValueError):
        max_subarray_sum([])