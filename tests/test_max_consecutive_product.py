import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_basic_positive_array():
    """Test with a basic array of positive integers"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    """Test array containing negative numbers"""
    arr = [-1, -2, -3, 4, 5]
    assert find_max_consecutive_product(arr) == 30  # -2 * -3 * 5

def test_array_with_zero():
    """Test array containing zero"""
    arr = [1, 0, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_mixed_numbers():
    """Test array with mixed positive, negative, and zero values"""
    arr = [-10, 5, 2, 3, -7]
    assert find_max_consecutive_product(arr) == 105  # 5 * 2 * 3

def test_minimum_array_length():
    """Test with minimum valid array length"""
    arr = [1, 2, 3]
    assert find_max_consecutive_product(arr) == 6  # 1 * 2 * 3

def test_too_short_array():
    """Test that ValueError is raised for array with fewer than 3 elements"""
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_consecutive_product([1, 2])

def test_large_numbers():
    """Test with large numbers"""
    arr = [1000, 1000, 1000, 1, 1]
    assert find_max_consecutive_product(arr) == 1_000_000_000  # 1000 * 1000 * 1000

def test_all_negative():
    """Test array with all negative numbers"""
    arr = [-5, -2, -1, -10, -3]
    assert find_max_consecutive_product(arr) == -30  # -5 * -2 * -1