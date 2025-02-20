import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test basic scenario of finding a missing number."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_sequential():
    """Test when numbers are close to sequential."""
    assert find_missing_number([3, 1, 2, 5]) == 4

def test_find_missing_number_first_missing():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_last_missing():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_unsorted():
    """Test with unsorted input."""
    assert find_missing_number([4, 1, 3, 5]) == 2

def test_find_missing_number_raises_on_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])