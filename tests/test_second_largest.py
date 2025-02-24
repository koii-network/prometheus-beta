import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test with a normal array of numbers"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 2, 1, 4]) == 4

def test_array_with_duplicates():
    """Test array with duplicate values"""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([4, 4, 3, 3, 2, 2, 1]) == 3

def test_negative_numbers():
    """Test array with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    assert find_second_largest([-10, 5, 0, 3, -5, 7]) == 5

def test_error_cases():
    """Test error cases"""
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single element array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Array with all same elements
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([2, 2, 2, 2])