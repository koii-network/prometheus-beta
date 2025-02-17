import pytest
from src.array_rotation import rotate_array_left

def test_rotate_array_left_normal_rotation():
    """Test standard array rotation"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 2)
    assert result == [3, 4, 5, 1, 2]

def test_rotate_array_left_full_rotation():
    """Test rotation equal to array length (should return original array)"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 5)
    assert result == arr

def test_rotate_array_left_partial_rotation():
    """Test rotation less than array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 1)
    assert result == [2, 3, 4, 5, 1]

def test_rotate_array_left_empty_array():
    """Test rotation on an empty array"""
    arr = []
    result = rotate_array_left(arr, 3)
    assert result == []

def test_rotate_array_left_mod_rotation():
    """Test rotation amount larger than array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 7)
    assert result == [3, 4, 5, 1, 2]

def test_rotate_array_left_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        rotate_array_left("not a list", 2)
    
    with pytest.raises(TypeError):
        rotate_array_left([1, 2, 3], "not an integer")

def test_rotate_array_left_negative_rotation():
    """Test negative rotation amount"""
    with pytest.raises(ValueError):
        rotate_array_left([1, 2, 3], -1)