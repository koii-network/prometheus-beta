import pytest
from src.array_rotation import rotate_array

def test_rotate_array_basic():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_array_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 5) == arr

def test_rotate_array_multiple_rotations():
    """Test rotation more than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 7) == [4, 5, 1, 2, 3]

def test_rotate_array_zero_rotation():
    """Test zero rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_rotate_array_empty_list():
    """Test rotation of empty list"""
    assert rotate_array([], 3) == []

def test_rotate_array_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_rotate_array_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_rotate_array_negative_rotation():
    """Test negative rotation amount"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)

def test_rotate_array_preserves_original():
    """Test that original array is not modified"""
    arr = [1, 2, 3, 4, 5]
    rotated = rotate_array(arr, 2)
    assert arr == [1, 2, 3, 4, 5]
    assert rotated == [4, 5, 1, 2, 3]