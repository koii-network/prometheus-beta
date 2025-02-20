import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4]) == 6

def test_array_with_negative_numbers():
    assert max_non_overlapping_subarray_sum([-1, -2, 3, 4]) == 7

def test_all_negative_numbers():
    assert max_non_overlapping_subarray_sum([-1, -2, -3]) == 0

def test_empty_array():
    assert max_non_overlapping_subarray_sum([]) == 0

def test_single_element_positive():
    assert max_non_overlapping_subarray_sum([5]) == 5

def test_single_element_negative():
    assert max_non_overlapping_subarray_sum([-5]) == 0

def test_mixed_positive_and_negative():
    assert max_non_overlapping_subarray_sum([1, -1, 2, -3, 4, 5]) == 9

def test_zero_sum_subarrays():
    assert max_non_overlapping_subarray_sum([0, 0, 0, 0]) == 0

def test_complex_case():
    assert max_non_overlapping_subarray_sum([3, 2, 7, 10, 4, 11, 15]) == 42