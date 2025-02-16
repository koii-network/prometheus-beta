import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4
    assert find_second_largest([10, 5, 8, 12, 3]) == 10

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values"""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 4, 4, 3, 3]) == 4

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([0, -1, -2, 1, 2]) == 0

def test_find_second_largest_insufficient_elements():
    """Test that ValueError is raised for insufficient unique elements"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1, 1, 1])
    
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5])
    
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])