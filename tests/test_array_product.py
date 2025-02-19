import pytest
from src.array_product import product_except_self

def test_product_except_self_basic():
    """Test basic functionality with standard input"""
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_product_except_self_with_zero():
    """Test input containing zero"""
    assert product_except_self([1, 0, 2, 3]) == [0, 6, 0, 0]

def test_product_except_self_negative_numbers():
    """Test input with negative numbers"""
    assert product_except_self([-1, -2, -3, -4]) == [-24, -12, -8, -6]

def test_product_except_self_mixed_numbers():
    """Test input with mixed positive and negative numbers"""
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_product_except_self_single_element():
    """Test single element list"""
    assert product_except_self([5]) == [1]

def test_product_except_self_empty_list():
    """Test empty list"""
    assert product_except_self([]) == []

def test_product_except_self_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        product_except_self("not a list")

def test_product_except_self_non_numeric():
    """Test non-numeric input raises ValueError"""
    with pytest.raises(ValueError):
        product_except_self([1, 2, "three", 4])