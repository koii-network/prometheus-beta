import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a simple sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_start():
    """Test when the missing number is at the start of the sequence."""
    assert find_missing_number([2, 3, 4, 5, 6]) == 1

def test_find_missing_number_end():
    """Test when the missing number is at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_sequence():
    """Test with a larger sequence of numbers."""
    test_arr = list(range(1, 11))
    test_arr.remove(7)
    assert find_missing_number(test_arr) == 7

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_invalid_input_non_integers():
    """Test that a list with non-integer elements raises a ValueError."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_missing_number([1, 2, '3', 4])

def test_single_element_list():
    """Test a list with a single element."""
    assert find_missing_number([2]) == 1