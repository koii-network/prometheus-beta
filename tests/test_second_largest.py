import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate numbers"""
    assert find_second_largest([1, 1, 2, 2, 3, 3, 4, 4, 5]) == 4
    assert find_second_largest([5, 5, 4, 4, 3, 3, 2, 2, 1]) == 4

def test_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, -3, -1, -2, -4]) == -2

def test_find_second_largest_error_cases():
    """Test error cases when array is too small or has no unique elements"""
    with pytest.raises(ValueError):
        find_second_largest([1])
    
    with pytest.raises(ValueError):
        find_second_largest([1, 1, 1, 1])

def test_find_second_largest_with_floats():
    """Test finding second largest with floating point numbers"""
    assert find_second_largest([1.5, 2.7, 3.2, 4.1, 5.0]) == 4.1