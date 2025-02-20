import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_full_range():
    """Test finding a missing number when the range starts from 1."""
    assert find_missing_number([2, 3, 4, 5, 6]) == 1

def test_find_missing_number_end_range():
    """Test finding a missing number at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_sequence():
    """Test finding a missing number in a larger sequence."""
    nums = list(range(1, 11))
    nums.remove(7)
    assert find_missing_number(nums) == 7

def test_find_missing_number_invalid_input():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])