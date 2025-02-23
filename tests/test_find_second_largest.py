import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_array():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 4, 3, 2, 1]) == 4
    assert find_second_largest([10, 5, 8, 12, 3]) == 10

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate numbers"""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 4, 4, 3, 3]) == 4

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, -4, -3, -2, -1]) == -2

def test_find_second_largest_error_cases():
    """Test error cases"""
    # Less than 2 elements
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single unique element
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1, 1, 1, 1])

def test_find_second_largest_floating_point():
    """Test with floating point numbers"""
    assert find_second_largest([1.5, 2.7, 0.3, 4.1]) == 2.7