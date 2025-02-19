import pytest
from src.max_product_consecutive import find_max_product_consecutive_three

def test_basic_positive_array():
    """Test with a basic array of positive integers"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_product_consecutive_three(arr) == 60

def test_mixed_integers():
    """Test with an array containing both positive and negative integers"""
    arr = [-1, 2, -3, 4, 5, -6]
    assert find_max_product_consecutive_three(arr) == 120

def test_zero_included():
    """Test with an array including zero"""
    arr = [1, 0, 2, 3, 4]
    assert find_max_product_consecutive_three(arr) == 0

def test_negative_numbers():
    """Test with an array of negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert find_max_product_consecutive_three(arr) == -6

def test_minimum_length():
    """Test with an array of exactly 3 elements"""
    arr = [1, 2, 3]
    assert find_max_product_consecutive_three(arr) == 6

def test_invalid_input():
    """Test that ValueError is raised for arrays with fewer than 3 elements"""
    with pytest.raises(ValueError):
        find_max_product_consecutive_three([1, 2])

def test_large_numbers():
    """Test with large positive and negative numbers"""
    arr = [1000, -500, 200, 300, -400, 500]
    assert find_max_product_consecutive_three(arr) == 30000000