import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending array"""
    arr = [1, 2, 4, 6, 7, 9, 10]
    assert find_missing_numbers(arr) == [3, 5, 8]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending array"""
    arr = [10, 9, 7, 5, 3, 1]
    assert find_missing_numbers(arr) == [8, 6, 4, 2]

def test_consecutive_numbers():
    """Test array with no missing numbers"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_single_element_array():
    """Test array with a single element"""
    arr = [5]
    assert find_missing_numbers(arr) == [1, 2, 3, 4]

def test_invalid_input_empty():
    """Test raising ValueError for empty list"""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_invalid_input_non_positive():
    """Test raising ValueError for non-positive integers"""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_negative_and_zero_input():
    """Test raising ValueError for non-positive input"""
    with pytest.raises(ValueError):
        find_missing_numbers([0, -1, 2, 3])