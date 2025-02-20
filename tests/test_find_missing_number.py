import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a basic scenario."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_sequential():
    """Test finding a missing number in a larger sequential range."""
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8]) == 3

def test_find_missing_number_last():
    """Test when the missing number is the last in the sequence."""
    assert find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 8

def test_find_missing_number_first():
    """Test when the missing number is the first in the sequence."""
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8]) == 1

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([])

def test_invalid_input_non_positive():
    """Test that a list with non-positive numbers raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([0, 1, 2, 3])
    
    with pytest.raises(ValueError):
        find_missing_number([-1, 2, 3, 4])

def test_invalid_input_non_integer():
    """Test that a list with non-integer elements raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, '3', 4])
    
    with pytest.raises(ValueError):
        find_missing_number([1.5, 2, 3, 4])