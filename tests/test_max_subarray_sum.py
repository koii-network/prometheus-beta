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
    with pytest.raises(ValueError):
        max_subarray_sum([])

def test_invalid_input_type():
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
        
def test_large_list():
    large_list = list(range(1000))  # List of 0 to 999
    assert max_subarray_sum(large_list) == sum(large_list)

def test_zeroes_and_negatives():
    assert max_subarray_sum([0, -1, 0, -2, 3, -3]) == 3