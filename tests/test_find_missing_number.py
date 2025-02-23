import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a simple sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_at_start():
    """Test when the missing number is at the start of the sequence."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_at_end():
    """Test when the missing number is at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_larger_range():
    """Test with a larger range of numbers."""
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3

def test_find_missing_number_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_find_missing_number_single_missing():
    """Ensure the function works with a single missing number."""
    nums = list(range(1, 11))
    nums.remove(7)
    assert find_missing_number(nums) == 7