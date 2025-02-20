import pytest
from src.odd_frequency import find_odd_frequency_number

def test_single_odd_frequency_number():
    """Test a list with one number appearing an odd number of times"""
    assert find_odd_frequency_number([1, 2, 2, 3, 3, 3, 4, 4]) == 1

def test_multiple_odd_frequency_numbers():
    """Test a list with multiple numbers appearing an odd number of times"""
    assert find_odd_frequency_number([1, 1, 2, 2, 3, 3, 3, 5, 5, 5]) == 3

def test_repeated_number_with_odd_frequency():
    """Test a list where a single number appears an odd number of times"""
    assert find_odd_frequency_number([5, 5, 5]) == 5

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_frequency_number([])

def test_no_odd_frequency_numbers_raises_error():
    """Test that a list with no odd frequency numbers raises a ValueError"""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_frequency_number([1, 1, 2, 2, 3, 3, 4, 4])