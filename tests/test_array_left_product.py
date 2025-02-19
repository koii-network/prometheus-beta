import pytest
from src.array_left_product import product_of_left_elements

def test_normal_array():
    assert product_of_left_elements([3, 1, 2, 5, 4]) == [1, 3, 3, 6, 30]

def test_sequential_array():
    assert product_of_left_elements([2, 4, 6, 8]) == [1, 2, 8, 48]

def test_empty_array():
    assert product_of_left_elements([]) == []

def test_single_element_array():
    assert product_of_left_elements([5]) == [1]

def test_array_with_zero():
    assert product_of_left_elements([1, 2, 0, 4, 5]) == [1, 1, 0, 0, 0]

def test_negative_numbers():
    assert product_of_left_elements([-1, 2, -3, 4]) == [1, -1, -2, -6]