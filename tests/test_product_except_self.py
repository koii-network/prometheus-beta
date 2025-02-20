import pytest
from src.product_except_self import product_except_self

def test_basic_case():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_single_element():
    assert product_except_self([5]) == [1]

def test_two_elements():
    assert product_except_self([2, 3]) == [3, 2]

def test_empty_list():
    assert product_except_self([]) == []

def test_with_zeros():
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]
    assert product_except_self([1, 0, 2, 3]) == [0, 6, 0, 0]

def test_with_negative_numbers():
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        product_except_self("not a list")

def test_invalid_list_elements():
    with pytest.raises(ValueError):
        product_except_self([1, 2, "3", 4])