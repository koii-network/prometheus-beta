import pytest
from src.max_product import max_product_of_two_numbers

def test_positive_numbers():
    """Test with a list of positive numbers"""
    assert max_product_of_two_numbers([1, 2, 3, 4, 5]) == 20

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    assert max_product_of_two_numbers([-5, -2, 1, 3, 4]) == 20

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_product_of_two_numbers([-10, -3, -5, -2]) == 30

def test_repeated_numbers():
    """Test with repeated numbers"""
    assert max_product_of_two_numbers([2, 2, 3, 3]) == 9

def test_only_two_numbers():
    """Test with only two numbers"""
    assert max_product_of_two_numbers([3, 4]) == 12

def test_zero_included():
    """Test when list includes zero"""
    assert max_product_of_two_numbers([-5, 0, 2, 3]) == 0

def test_insufficient_numbers():
    """Test that ValueError is raised for lists with fewer than 2 numbers"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([5])

def test_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([])