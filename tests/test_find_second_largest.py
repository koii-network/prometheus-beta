import pytest
from src.find_second_largest import find_second_largest

def test_unsorted_array():
    """Test finding second largest in an unsorted array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_array_with_duplicates():
    """Test finding second largest when array contains duplicates"""
    assert find_second_largest([5, 5, 8, 8, 9, 1]) == 8

def test_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -5, -3, -2, -8]) == -2

def test_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers"""
    assert find_second_largest([-10, 5, 0, 15, 3]) == 5

def test_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_second_largest([])

def test_single_unique_element():
    """Test that an array with only one unique element raises a ValueError"""
    with pytest.raises(ValueError, match="Array must contain at least two unique elements"):
        find_second_largest([5, 5, 5, 5])