import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_array():
    """Test finding second largest in a normal array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest when there are duplicate numbers"""
    assert find_second_largest([5, 5, 2, 8, 8, 1, 9]) == 8

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -5, -2, -8, -3]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers"""
    assert find_second_largest([-1, 0, 5, 2, 8, 1, 9]) == 8

def test_find_second_largest_raises_error_with_insufficient_unique_elements():
    """Test that an error is raised when there are not enough unique elements"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5, 5])

def test_find_second_largest_raises_error_with_single_element():
    """Test that an error is raised with a single element"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5])

def test_find_second_largest_empty_array():
    """Test that an error is raised with an empty array"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])