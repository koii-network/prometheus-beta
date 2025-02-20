import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard case."""
    arr = [1, 2, 4, 5, 6, 7, 8]
    assert find_missing_number(arr) == 3

def test_find_missing_number_start():
    """Test finding a missing number at the start of the sequence."""
    arr = [2, 3, 4, 5, 6, 7, 8]
    assert find_missing_number(arr) == 1

def test_find_missing_number_end():
    """Test finding a missing number at the end of the sequence."""
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert find_missing_number(arr) == 8

def test_find_missing_number_one_element():
    """Test with an array where a single number is missing."""
    arr = [2]
    assert find_missing_number(arr) == 1

def test_find_missing_number_invalid_input():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])