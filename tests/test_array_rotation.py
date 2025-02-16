import pytest
from src.array_rotation import rotate_array_left

def test_rotate_array_basic():
    """Test basic array rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotate_array_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_rotate_array_zero_rotation():
    """Test zero rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_rotate_array_excess_rotation():
    """Test rotation greater than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_rotate_empty_array():
    """Test rotation of an empty array"""
    arr = []
    assert rotate_array_left(arr, 3) == []

def test_rotate_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_rotate_invalid_rotation_type():
    """Test error handling for non-integer rotation amount"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_rotate_negative_rotation():
    """Test error handling for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)