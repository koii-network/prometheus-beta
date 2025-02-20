import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test finding duplicates in a simple list."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_find_duplicates_no_duplicates():
    """Test with a list that has no duplicates."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_all_duplicates():
    """Test with a list where all elements are duplicates."""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_find_duplicates_empty_list():
    """Test with an empty list."""
    assert find_duplicates([]) == []

def test_find_duplicates_multiple_duplicates():
    """Test with multiple duplicates of different values."""
    assert find_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]

def test_find_duplicates_negative_numbers():
    """Test with negative numbers."""
    assert find_duplicates([-1, -1, 0, 0, 1, 1]) == [-1, 0, 1]