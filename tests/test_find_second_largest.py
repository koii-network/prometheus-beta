import pytest
from src.find_second_largest import find_second_largest

def test_normal_array():
    """Test with a normal unsorted array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_array_with_duplicates():
    """Test array with duplicate elements"""
    assert find_second_largest([5, 5, 2, 8, 1, 9, 9]) == 8

def test_negative_numbers():
    """Test array with negative numbers"""
    assert find_second_largest([-1, -5, -2, -8, -9]) == -2

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    assert find_second_largest([-1, 5, 0, 8, 3]) == 5

def test_already_sorted():
    """Test array that is already sorted"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_error_on_single_element():
    """Test error raised when array has only one unique element"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])

def test_error_on_empty_array():
    """Test error raised when array is empty"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])