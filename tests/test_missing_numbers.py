import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]

def test_no_missing_numbers():
    """Test an array with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_large_gaps():
    """Test an array with large gaps between numbers."""
    assert find_missing_numbers([2, 5, 8, 11]) == [3, 4, 6, 7, 9, 10]

def test_single_element():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == [1, 2, 3, 4]

def test_invalid_input_empty():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_invalid_input_non_positive():
    """Test that a list with non-positive numbers raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_non_integer_input():
    """Test that a list with non-integer inputs raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, '3', 4])

def test_large_sorted_range():
    """Test a larger sorted range with missing numbers."""
    assert find_missing_numbers([1, 3, 5, 10, 15, 20]) == [2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]