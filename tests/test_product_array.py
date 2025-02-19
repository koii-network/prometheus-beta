import pytest
from src.product_array import calculate_left_product_array

def test_normal_case():
    """Test with a normal list of numbers"""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 1, 2, 6, 24]
    assert calculate_left_product_array(input_list) == expected

def test_empty_list():
    """Test with an empty list"""
    assert calculate_left_product_array([]) == []

def test_single_element():
    """Test with a single element list"""
    assert calculate_left_product_array([42]) == [1]

def test_with_zeros():
    """Test a list containing zeros"""
    input_list = [1, 0, 2, 3, 4]
    expected = [1, 0, 0, 0, 0]
    assert calculate_left_product_array(input_list) == expected

def test_with_negative_numbers():
    """Test with negative numbers"""
    input_list = [-1, 2, -3, 4, -5]
    expected = [1, -1, -2, -6, -24]
    assert calculate_left_product_array(input_list) == expected

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        calculate_left_product_array(42)

def test_non_numeric_elements():
    """Test raising ValueError for non-numeric elements"""
    with pytest.raises(ValueError):
        calculate_left_product_array([1, 2, 'a', 4, 5])