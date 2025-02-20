import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_basic():
    """Test finding second largest in a basic unsorted array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_sorted():
    """Test finding second largest in a sorted array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate elements"""
    assert find_second_largest([5, 5, 3, 3, 2, 1]) == 3

def test_find_second_largest_with_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -5, -2, -8, -3]) == -2

def test_find_second_largest_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([])

def test_find_second_largest_single_element():
    """Test that an array with a single element raises a ValueError"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([1])

def test_find_second_largest_all_same_elements():
    """Test that an array with all same elements raises a ValueError"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])