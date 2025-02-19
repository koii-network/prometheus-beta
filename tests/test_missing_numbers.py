import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    # Test ascending array with missing numbers
    assert find_missing_numbers([1, 2, 4, 6, 7, 9, 10]) == [3, 5, 8]

def test_missing_numbers_descending():
    # Test descending array with missing numbers
    assert find_missing_numbers([10, 9, 7, 6, 4, 2, 1]) == [8, 5, 3]

def test_no_missing_numbers_ascending():
    # Test ascending array with no missing numbers
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_no_missing_numbers_descending():
    # Test descending array with no missing numbers
    assert find_missing_numbers([5, 4, 3, 2, 1]) == []

def test_single_element():
    # Test array with a single element
    assert find_missing_numbers([5]) == [1, 2, 3, 4]

def test_invalid_input():
    # Test empty list
    with pytest.raises(ValueError):
        find_missing_numbers([])
    
    # Test list with non-positive integers
    with pytest.raises(ValueError):
        find_missing_numbers([0, -1, 2])
    
    # Test list with non-integers
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, '3'])