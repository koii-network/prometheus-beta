import pytest
from src.product_array_left import product_array_left

def test_product_array_left_basic():
    """Test with a standard numeric array"""
    assert product_array_left([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_product_array_left_with_zeroes():
    """Test an array containing zeroes"""
    assert product_array_left([1, 0, 2, 3]) == [1, 0, 0, 0]

def test_product_array_left_single_element():
    """Test a single-element array"""
    assert product_array_left([5]) == [1]

def test_product_array_left_empty_list():
    """Test an empty list"""
    assert product_array_left([]) == [1]

def test_product_array_left_negative_numbers():
    """Test an array with negative numbers"""
    assert product_array_left([-1, 2, -3, 4]) == [1, -1, -2, -6]

def test_product_array_left_float_numbers():
    """Test an array with floating point numbers"""
    assert product_array_left([1.5, 2.0, 3.0]) == [1, 1.5, 3.0]

def test_product_array_left_invalid_input_type():
    """Test with non-list input"""
    with pytest.raises(TypeError):
        product_array_left("not a list")

def test_product_array_left_non_numeric_elements():
    """Test with non-numeric list elements"""
    with pytest.raises(ValueError):
        product_array_left([1, 2, 'a', 4])