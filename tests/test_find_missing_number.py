import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_standard_case():
    """Test finding a missing number in a standard sequence."""
    nums = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    assert find_missing_number(nums) == 3

def test_find_missing_number_first_missing():
    """Test when the first number is missing."""
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_missing_number(nums) == 1

def test_find_missing_number_last_missing():
    """Test when the last number is missing."""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_missing_number(nums) == 10

def test_find_missing_number_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_find_missing_number_single_element():
    """Test a case with only one element."""
    nums = [2]
    assert find_missing_number(nums) == 1

def test_find_missing_number_consecutive_case():
    """Test a case with mostly consecutive numbers."""
    nums = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_missing_number(nums) == 2