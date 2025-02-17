import pytest
from src.array_rotator import rotate_array_left

def test_rotate_array_left_basic():
    """Test basic array rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotate_array_left_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_rotate_array_left_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_rotate_array_left_over_rotation():
    """Test rotation greater than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_rotate_array_left_empty():
    """Test rotation of empty array"""
    arr = []
    assert rotate_array_left(arr, 3) == []

def test_rotate_array_left_invalid_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        rotate_array_left("not a list", 2)

def test_rotate_array_left_negative_rotation():
    """Test handling of negative rotation amount"""
    with pytest.raises(ValueError):
        rotate_array_left([1, 2, 3], -1)

def test_rotate_array_left_non_integer_rotation():
    """Test handling of non-integer rotation amount"""
    with pytest.raises(TypeError):
        rotate_array_left([1, 2, 3], "2")