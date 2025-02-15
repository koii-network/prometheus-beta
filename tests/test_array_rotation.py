import pytest
from src.array_rotation import rotate_array_left

def test_rotate_array_left_basic():
    """Test basic array rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotate_array_left_zero():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_rotate_array_left_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_rotate_array_left_overflow():
    """Test rotation more than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_rotate_array_left_empty():
    """Test rotation of empty array"""
    arr = []
    assert rotate_array_left(arr, 3) == []

def test_rotate_array_left_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_rotate_array_left_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "two")