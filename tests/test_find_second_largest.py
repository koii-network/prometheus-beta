import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values"""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2

def test_find_second_largest_unsorted():
    """Test finding second largest in an unsorted array"""
    assert find_second_largest([9, 3, 7, 1, 8, 4]) == 8

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -5, -3, -2, -4]) == -2

def test_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])

def test_single_element_array():
    """Test that an array with a single unique element raises a ValueError"""
    with pytest.raises(ValueError, match="Array must have at least two unique elements"):
        find_second_largest([42])

def test_single_value_repeated():
    """Test that an array with a single repeated value raises a ValueError"""
    with pytest.raises(ValueError, match="Array must have at least two unique elements"):
        find_second_largest([7, 7, 7, 7])