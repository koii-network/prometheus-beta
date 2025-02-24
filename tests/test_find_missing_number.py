import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_at_end():
    """Test when the missing number is the last in the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_at_start():
    """Test when the missing number is the first in the sequence."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number([])

def test_invalid_input_not_a_list():
    """Test that non-list input raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_number(None)

def test_find_missing_number_large_sequence():
    """Test with a larger sequence."""
    large_seq = list(range(1, 10)) + list(range(11, 11))
    assert find_missing_number(large_seq) == 10