import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding missing number in a typical scenario."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_full_range():
    """Test finding missing number in a full range scenario."""
    assert find_missing_number([1, 2, 4, 5, 3, 7]) == 6

def test_find_missing_number_lowest_missing():
    """Test finding missing number when the lowest number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_highest_missing():
    """Test finding missing number when the highest number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([])

def test_invalid_input_non_positive():
    """Test that a list with non-positive numbers raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 3, 0])
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 3, -1])

def test_invalid_input_non_integers():
    """Test that a list with non-integer values raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 3, '4'])
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 3, 3.14])