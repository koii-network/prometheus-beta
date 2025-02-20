import pytest
from src.sum_odd_even import sum_odd_even

def test_sum_odd_even_mixed_numbers():
    result = sum_odd_even([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)

def test_sum_odd_even_only_odd():
    result = sum_odd_even([1, 3, 5, 7])
    assert result == (16, 0)

def test_sum_odd_even_only_even():
    result = sum_odd_even([2, 4, 6, 8])
    assert result == (0, 20)

def test_sum_odd_even_empty_array():
    result = sum_odd_even([])
    assert result == (0, 0)

def test_sum_odd_even_negative_numbers():
    result = sum_odd_even([-1, -2, -3, -4, -5])
    assert result == (-9, -6)

def test_sum_odd_even_mixed_negative_positive():
    result = sum_odd_even([-1, 2, -3, 4, 5, -6])
    assert result == (1, 0)