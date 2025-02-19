import pytest
from src.left_product_array import calculate_left_product_array

def test_basic_array():
    assert calculate_left_product_array([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_single_element_array():
    assert calculate_left_product_array([5]) == [1]

def test_empty_array():
    assert calculate_left_product_array([]) == []

def test_array_with_zeros():
    assert calculate_left_product_array([1, 0, 2, 3]) == [1, 1, 0, 0]

def test_array_with_negative_numbers():
    assert calculate_left_product_array([-1, 2, -3, 4]) == [1, -1, -2, -6]

def test_large_number_array():
    arr = [10, 20, 30, 40, 50]
    assert calculate_left_product_array(arr) == [1, 10, 200, 6000, 240000]