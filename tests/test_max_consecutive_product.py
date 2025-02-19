import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_basic_positive_array():
    """Test with a basic positive integer array"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_negative_and_positive_mix():
    """Test with mix of negative and positive integers"""
    arr = [-1, 2, -3, 4, 5, -6]
    assert find_max_consecutive_product(arr) == 6  # Current max of first few windows

def test_with_zeros():
    """Test array containing zeros"""
    arr = [0, 1, 2, 3, 0, 4, 5]
    assert find_max_consecutive_product(arr) == 6  # One of the windows

def test_all_negative_numbers():
    """Test with all negative numbers"""
    arr = [-5, -2, -1, -3, -4]
    assert find_max_consecutive_product(arr) == -6  # -2 * -1 * -3

def test_array_too_small():
    """Test that ValueError is raised for arrays with fewer than 3 elements"""
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_consecutive_product([1, 2])

def test_large_numbers():
    """Test with large numbers to ensure no integer overflow"""
    arr = [1000, 1000, 1000, 1, 1, 1]
    assert find_max_consecutive_product(arr) == 1_000_000_000  # 1000 * 1000 * 1000

def test_single_product_is_max():
    """Test where the first or last three-element group is the max"""
    arr = [10, 3, 5, 2, 1, 1]
    assert find_max_consecutive_product(arr) == 150  # 10 * 3 * 5