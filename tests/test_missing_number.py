import pytest
from src.missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard scenario."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_at_beginning():
    """Test when the missing number is at the beginning of the range."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_at_end():
    """Test when the missing number is at the end of the range."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_range():
    """Test with a larger range of numbers."""
    nums = [x for x in range(1, 11) if x != 7]
    assert find_missing_number(nums) == 7

def test_find_missing_number_empty_input():
    """Test that an empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_find_missing_number_out_of_range():
    """Test that numbers outside the valid range raise a ValueError."""
    with pytest.raises(ValueError, match="All numbers must be between"):
        find_missing_number([0, 1, 2, 3])
    
    with pytest.raises(ValueError, match="All numbers must be between"):
        find_missing_number([1, 2, 3, 6])

def test_find_missing_number_duplicates():
    """Test that the function works with unique numbers."""
    with pytest.raises(ValueError, match="All numbers must be between"):
        find_missing_number([1, 2, 2, 4])  # Duplicates are not allowed