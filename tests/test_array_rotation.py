import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotation_zero():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_rotation_over_length():
    """Test rotation more than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of empty array"""
    arr = []
    assert rotate_array_left(arr, 2) == []

def test_invalid_input_type():
    """Test invalid array input type"""
    with pytest.raises(TypeError):
        rotate_array_left("not a list", 2)

def test_invalid_rotation_type():
    """Test invalid rotation amount type"""
    with pytest.raises(TypeError):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount"""
    with pytest.raises(ValueError):
        rotate_array_left([1, 2, 3], -1)