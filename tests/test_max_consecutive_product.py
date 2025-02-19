import pytest
from src.max_consecutive_product import max_product_consecutive_three

def test_positive_integers():
    """Test with an array of positive integers"""
    arr = [1, 2, 3, 4, 5]
    assert max_product_consecutive_three(arr) == 60  # 3 * 4 * 5

def test_mixed_integers():
    """Test with mixed positive and negative integers"""
    arr = [-1, 2, 3, -4, 5]
    assert max_product_consecutive_three(arr) == -6  # -1 * 2 * 3

def test_negative_integers():
    """Test with array containing all negative integers"""
    arr = [-10, -5, -2, -1, -3]
    assert max_product_consecutive_three(arr) == -6  # -2 * -1 * -3

def test_with_zero():
    """Test with an array containing zero"""
    arr = [1, 0, 3, 4, 5]
    assert max_product_consecutive_three(arr) == 60  # 3 * 4 * 5

def test_minimum_length():
    """Test with minimum required length"""
    arr = [1, 2, 3]
    assert max_product_consecutive_three(arr) == 6  # 1 * 2 * 3

def test_too_short_array():
    """Test that ValueError is raised for arrays with fewer than 3 elements"""
    with pytest.raises(ValueError):
        max_product_consecutive_three([1, 2])

def test_large_numbers():
    """Test with large numbers to simulate large array scenario"""
    arr = [1000000, 1000000, 1000000, 1, 1]
    assert max_product_consecutive_three(arr) == 1000000 ** 3