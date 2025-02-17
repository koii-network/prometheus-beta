import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_basic():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate numbers"""
    assert find_second_largest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers"""
    assert find_second_largest([-10, 0, 5, 3, -5, 10]) == 5

def test_find_second_largest_error_cases():
    """Test error cases"""
    # Single element array should raise ValueError
    with pytest.raises(ValueError):
        find_second_largest([1])
    
    # Array with all same elements should raise ValueError
    with pytest.raises(ValueError):
        find_second_largest([2, 2, 2, 2])

def test_find_second_largest_edge_cases():
    """Test edge cases"""
    assert find_second_largest([1, 1, 2]) == 1
    assert find_second_largest([10, 10, 9, 8, 8]) == 9