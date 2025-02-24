import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal unsorted array."""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest when array contains duplicates."""
    assert find_second_largest([5, 5, 2, 8, 1, 9, 9]) == 8

def test_find_second_largest_all_same():
    """Test that an error is raised when all elements are the same."""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])

def test_find_second_largest_empty_array():
    """Test that an error is raised for an empty array."""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([])

def test_find_second_largest_single_element():
    """Test that an error is raised for a single-element array."""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([42])

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -5, -2, -8, -9]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers."""
    assert find_second_largest([-1, 5, 0, 8, -9]) == 5