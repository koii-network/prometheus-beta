import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_numeric_string():
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_mixed_string():
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_with_leading_zeros():
    assert sum_of_digits('00123') == 6

def test_sum_of_digits_no_digits():
    assert sum_of_digits('abcdef') == 0

def test_sum_of_digits_empty_string():
    assert sum_of_digits('') == 0

def test_sum_of_digits_single_digit():
    assert sum_of_digits('5') == 5

def test_sum_of_digits_complex_string():
    assert sum_of_digits('a1b2c3d4e5f') == 15