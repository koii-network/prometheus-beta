import pytest
from src.product_left_array import product_left_array

def test_product_left_array_basic():
    """Test basic functionality of the product_left_array function."""
    assert product_left_array([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_product_left_array_empty():
    """Test with an empty list."""
    assert product_left_array([]) == []

def test_product_left_array_single_element():
    """Test with a single element list."""
    assert product_left_array([5]) == [1]

def test_product_left_array_with_zeros():
    """Test with zeros in the input list."""
    assert product_left_array([1, 0, 2, 3]) == [1, 0, 0, 0]

def test_product_left_array_negative_numbers():
    """Test with negative numbers."""
    assert product_left_array([-1, 2, -3, 4]) == [1, -1, -2, -6]

def test_product_left_array_large_list():
    """Test with a larger list of numbers."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 1, 2, 6, 24]
    assert product_left_array(input_list) == expected