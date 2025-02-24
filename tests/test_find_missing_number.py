import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test basic functionality of finding a missing number."""
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5]) == 6

def test_find_missing_number_sequential():
    """Test with a nearly sequential list."""
    assert find_missing_number([1, 2, 4, 6, 3, 7, 8]) == 5

def test_find_missing_number_sorted():
    """Test with a sorted list of numbers."""
    assert find_missing_number([1, 2, 3, 4, 6, 7, 8, 9]) == 5

def test_find_missing_number_first_missing():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8]) == 1

def test_find_missing_number_last_missing():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 8

def test_find_missing_number_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])