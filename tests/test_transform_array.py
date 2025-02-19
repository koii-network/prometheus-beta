import pytest
from src.transform_array import transform_array

def test_transform_array_zero_elements():
    """Test array with zero elements"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_positive_numbers():
    """Test array with positive numbers"""
    assert transform_array([1, 2, 3]) == [2, 5, 10]

def test_transform_array_mixed_numbers():
    """Test array with mixed zero and non-zero numbers"""
    assert transform_array([0, 1, 2, 0, 3]) == [0, 2, 5, 0, 10]

def test_transform_array_empty():
    """Test empty array"""
    assert transform_array([]) == []

def test_transform_array_invalid_input():
    """Test negative number input raises ValueError"""
    with pytest.raises(ValueError, match="Input must be an array of non-negative integers"):
        transform_array([-1, 2, 3])

def test_transform_array_invalid_type():
    """Test non-integer input raises ValueError"""
    with pytest.raises(ValueError, match="Input must be an array of non-negative integers"):
        transform_array([1, 2, 'a'])