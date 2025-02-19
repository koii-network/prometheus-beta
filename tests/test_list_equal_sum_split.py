import pytest
from src.list_equal_sum_split import can_split_into_equal_sum_sublists

def test_can_split_equal_sum_basic_true():
    assert can_split_into_equal_sum_sublists([1, 2, 3, 4, 5, 5]) is True

def test_can_split_equal_sum_basic_false():
    assert can_split_into_equal_sum_sublists([1, 2, 3, 4]) is False

def test_can_split_equal_sum_empty_list():
    assert can_split_into_equal_sum_sublists([]) is False

def test_can_split_equal_sum_odd_total():
    assert can_split_into_equal_sum_sublists([1, 3, 5]) is False

def test_can_split_equal_sum_single_element():
    assert can_split_into_equal_sum_sublists([1]) is False

def test_can_split_equal_sum_all_zeros():
    assert can_split_into_equal_sum_sublists([0, 0, 0, 0]) is True

def test_can_split_equal_sum_negative_numbers():
    assert can_split_into_equal_sum_sublists([-1, 1, 2, -2]) is True

def test_can_split_equal_sum_complex_case():
    assert can_split_into_equal_sum_sublists([3, 1, 1, 2, 2, 1]) is True