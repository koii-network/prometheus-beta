import pytest
from src.product_except_self import product_except_self

def test_standard_input():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_empty_list():
    assert product_except_self([]) == []

def test_single_element():
    assert product_except_self([5]) == [1]

def test_two_elements():
    assert product_except_self([2, 3]) == [3, 2]

def test_zero_in_list():
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]

def test_negative_numbers():
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_float_numbers():
    assert product_except_self([1.5, 2.5, 3.5]) == [8.75, 5.25, 3.75]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        product_except_self("not a list")

def test_non_numeric_elements():
    with pytest.raises(ValueError):
        product_except_self([1, 2, "three", 4])