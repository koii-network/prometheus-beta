import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_basic_positive_array():
    """Test with a basic array of positive integers"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    """Test an array containing negative numbers"""
    arr = [-1, -2, -3, 4, 5, 6]
    assert find_max_consecutive_product(arr) == 90  # 4 * 5 * 6

def test_array_with_zeros():
    """Test an array containing zeros"""
    arr = [1, 2, 0, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_mixed_values():
    """Test an array with mixed positive, negative, and zero values"""
    arr = [-10, 5, 2, 0, -6, 4, 3]
    assert find_max_consecutive_product(arr) == 0  # 0 * -6 * 4

def test_minimum_length():
    """Test with minimum length array (3 elements)"""
    arr = [1, 2, 3]
    assert find_max_consecutive_product(arr) == 6

def test_error_on_short_array():
    """Test that an error is raised for arrays with fewer than 3 elements"""
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_consecutive_product([1, 2])

def test_large_values():
    """Test with large integers"""
    arr = [1000000, 1000000, 1000000, 1, 1]
    assert find_max_consecutive_product(arr) == 1000000 ** 3