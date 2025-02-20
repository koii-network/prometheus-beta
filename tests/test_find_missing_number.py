import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5]) == 6

def test_find_missing_number_consecutive():
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8]) == 3

def test_find_missing_number_at_start():
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8]) == 1

def test_find_missing_number_at_end():
    assert find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 8

def test_find_missing_number_two_elements():
    assert find_missing_number([2]) == 1
    assert find_missing_number([1]) == 2

def test_find_missing_number_error_empty_list():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_find_missing_number_error_invalid_range():
    with pytest.raises(ValueError, match="No valid missing number found"):
        find_missing_number([10, 11, 12])  # Numbers outside valid range