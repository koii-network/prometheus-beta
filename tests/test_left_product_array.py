import pytest
from src.left_product_array import left_product_array

def test_standard_array():
    """Test a standard array with multiple elements"""
    assert left_product_array([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_empty_array():
    """Test an empty array"""
    assert left_product_array([]) == []

def test_single_element_array():
    """Test an array with a single element"""
    assert left_product_array([5]) == [1]

def test_array_with_zeros():
    """Test an array that includes zeros"""
    assert left_product_array([1, 0, 2, 3]) == [1, 0, 0, 0]

def test_negative_numbers():
    """Test an array with negative numbers"""
    assert left_product_array([-1, 2, -3, 4]) == [1, -1, -2, -6]

def test_large_numbers():
    """Test an array with larger numbers"""
    assert left_product_array([10, 20, 30, 40]) == [1, 10, 200, 6000]