import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9

def test_array_with_negative_numbers():
    assert max_non_overlapping_subarray_sum([-1, 2, -3, 4, -5]) == 4

def test_all_negative_numbers():
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == 0

def test_single_element_array():
    assert max_non_overlapping_subarray_sum([10]) == 10

def test_empty_array():
    assert max_non_overlapping_subarray_sum([]) == 0

def test_mixed_positive_negative():
    assert max_non_overlapping_subarray_sum([5, -3, 4, -1, 3, -2]) == 9

def test_invalid_input_type():
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum("not a list")

def test_large_numbers():
    assert max_non_overlapping_subarray_sum([1000, -2000, 3000, -4000, 5000]) == 6000