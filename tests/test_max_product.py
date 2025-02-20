import pytest
from src.max_product import max_product_of_two_numbers

def test_positive_numbers():
    """Test with a list of positive numbers"""
    assert max_product_of_two_numbers([1, 2, 3, 4, 5]) == 20

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    assert max_product_of_two_numbers([-10, -5, 2, 3, 4]) == 50

def test_negative_numbers():
    """Test with a list of negative numbers"""
    assert max_product_of_two_numbers([-5, -2, -10, -1]) == 50

def test_two_numbers():
    """Test with exactly two numbers"""
    assert max_product_of_two_numbers([3, 4]) == 12

def test_error_on_single_number():
    """Test that an error is raised when list has fewer than two numbers"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([5])

def test_error_on_empty_list():
    """Test that an error is raised on an empty list"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([])