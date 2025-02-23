import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test basic functionality of finding a missing number."""
    assert find_missing_number([1, 3, 4, 5]) == 2
    assert find_missing_number([2, 3, 4, 5]) == 1
    assert find_missing_number([1, 2, 3, 5]) == 4

def test_find_missing_number_consecutive():
    """Test with consecutive numbers."""
    assert find_missing_number([1, 2, 4, 5, 6]) == 3

def test_find_missing_number_edge_cases():
    """Test various edge cases."""
    assert find_missing_number([2]) == 1
    assert find_missing_number([1]) == 2

def test_find_missing_number_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])