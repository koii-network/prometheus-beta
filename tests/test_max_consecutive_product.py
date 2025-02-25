import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_typical_positive_array():
    """Test with a typical array of positive integers"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    """Test array containing negative numbers"""
    arr = [-1, -2, -3, 4, 5]
    assert find_max_consecutive_product(arr) == 24  # 4 * 5 * x

def test_array_with_zero():
    """Test array containing zero"""
    arr = [1, 0, 2, 3, 4]
    assert find_max_consecutive_product(arr) == 24  # 2 * 3 * 4

def test_array_with_negative_and_zero():
    """Test array with negative numbers and zero"""
    arr = [-1, 0, 2, 3, -4]
    assert find_max_consecutive_product(arr) == 24  # 2 * 3 * 4

def test_small_array():
    """Test array with less than 3 elements"""
    arr = [1, 2]
    assert find_max_consecutive_product(arr) is None

def test_single_element_array():
    """Test array with single element"""
    arr = [5]
    assert find_max_consecutive_product(arr) is None

def test_large_magnitude_numbers():
    """Test array with large magnitude numbers"""
    arr = [1000000, -1000000, 1000000, 2, 3]
    assert find_max_consecutive_product(arr) == 6000000  # 1000000 * 1000000 * 6

def test_all_negative_array():
    """Test array with all negative numbers"""
    arr = [-5, -2, -1, -3, -4]
    assert find_max_consecutive_product(arr) == 6  # -2 * -1 * -3

def test_large_array():
    """Test performance with a larger array"""
    arr = list(range(1000))  # 0 to 999
    # Expected to work without performance issues
    result = find_max_consecutive_product(arr)
    assert result is not None