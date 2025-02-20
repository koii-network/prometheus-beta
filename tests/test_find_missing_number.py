import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard case."""
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5]) == 6

def test_find_missing_number_start():
    """Test when the missing number is at the start of the range."""
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8]) == 1

def test_find_missing_number_end():
    """Test when the missing number is at the end of the range."""
    assert find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 8

def test_find_missing_number_small_array():
    """Test with a small array."""
    assert find_missing_number([2, 1]) == 3

def test_find_missing_number_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([])