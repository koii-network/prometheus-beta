import pytest
from src.array_difference import calculate_array_difference

def test_basic_array_difference():
    """Test basic array difference calculation"""
    A = [5, 7, 3, 9, 2, 6, 8, 1, 4, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [4, 5, 0, 5, 0, 0, 1, 3, 5, 0]
    assert calculate_array_difference(A, B) == expected

def test_negative_difference():
    """Test scenarios where difference results in negative values"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [5, 7, 3, 9, 2, 6, 8, 1, 4, 0]
    expected = [6, 5, 0, 5, 3, 0, 0, 7, 5, 0]
    assert calculate_array_difference(A, B) == expected

def test_zero_difference():
    """Test array difference with zero values"""
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert calculate_array_difference(A, B) == expected

def test_maximum_values():
    """Test array difference with maximum values"""
    A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]
    assert calculate_array_difference(A, B) == expected

def test_invalid_array_length():
    """Test error handling for invalid array lengths"""
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        calculate_array_difference([1, 2, 3], [4, 5, 6])
    
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        calculate_array_difference([1]*11, [2]*11)