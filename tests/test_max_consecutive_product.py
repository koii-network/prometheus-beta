import pytest
from src.max_consecutive_product import max_consecutive_product

def test_basic_positive_array():
    """Test with a basic array of positive numbers"""
    arr = [1, 2, 3, 4, 5]
    assert max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    """Test array containing negative numbers"""
    arr = [-1, -2, -3, 4, 5]
    assert max_consecutive_product(arr) == 24  # -2 * -3 * 4

def test_array_with_zeros():
    """Test array containing zeros"""
    arr = [1, 0, 2, 3, 4]
    assert max_consecutive_product(arr) == 24  # 2 * 3 * 4

def test_all_negative_array():
    """Test array with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert max_consecutive_product(arr) == -6  # -2 * -3 * -1

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    arr = [-10, 5, 2, 3, 7, -1]
    assert max_consecutive_product(arr) == 42  # realistic max consecutive product

def test_minimum_length_array():
    """Test minimum valid array length"""
    arr = [1, 2, 3]
    assert max_consecutive_product(arr) == 6  # 1 * 2 * 3

def test_invalid_short_array():
    """Test that too short an array raises an error"""
    with pytest.raises(ValueError):
        max_consecutive_product([1, 2])

def test_empty_array():
    """Test that an empty array raises an error"""
    with pytest.raises(ValueError):
        max_consecutive_product([])