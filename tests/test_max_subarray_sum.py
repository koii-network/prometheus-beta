import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_positive_numbers():
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9
    assert max_non_overlapping_subarray_sum([5, 5, 5, 5, 5]) == 15

def test_mixed_numbers():
    assert max_non_overlapping_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_non_overlapping_subarray_sum([1, -2, 3, 4, -5, 6]) == 9

def test_negative_numbers():
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == 0
    assert max_non_overlapping_subarray_sum([-10, 5, -15, 7]) == 5

def test_single_element():
    assert max_non_overlapping_subarray_sum([10]) == 10
    assert max_non_overlapping_subarray_sum([-5]) == 0

def test_two_elements():
    assert max_non_overlapping_subarray_sum([1, 2]) == 2
    assert max_non_overlapping_subarray_sum([-1, 2]) == 2

def test_input_validation():
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum("not a list")
    
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum([])

def test_zero_elements():
    assert max_non_overlapping_subarray_sum([0, 0, 0]) == 0
    assert max_non_overlapping_subarray_sum([0, -1, 0]) == 0