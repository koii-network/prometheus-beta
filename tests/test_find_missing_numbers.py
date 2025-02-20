import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a standard case"""
    arr = [1, 3, 5, 7, 10]
    assert find_missing_numbers(arr) == [2, 4, 6, 8, 9]

def test_find_missing_numbers_consecutive():
    """Test an array with no missing numbers"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_large_range():
    """Test finding missing numbers in a larger range"""
    arr = [10, 20, 30, 50, 100]
    expected = list(range(11, 20)) + list(range(21, 30)) + list(range(31, 50)) + list(range(51, 100))
    assert find_missing_numbers(arr) == expected

def test_find_missing_numbers_single_element():
    """Test an array with a single element"""
    arr = [5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])