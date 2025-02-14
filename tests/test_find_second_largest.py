import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 5, 4, 3, 2, 1]) == 4
    assert find_second_largest([10, 5, 8, 12, 3]) == 10

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values"""
    assert find_second_largest([7, 7, 5, 5, 3, 3]) == 5

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers"""
    assert find_second_largest([-10, 5, 0, -5, 10]) == 5

def test_find_second_largest_error_cases():
    """Test error cases"""
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single element array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Array with all same elements
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])