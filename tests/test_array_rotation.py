import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 2)
    assert result == [3, 4, 5, 1, 2]

def test_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 0)
    assert result == arr
    assert result is not arr  # Ensure a new list is returned

def test_full_array_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 5)
    assert result == arr

def test_rotation_beyond_length():
    """Test rotation with n greater than array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 7)  # 7 % 5 = 2
    assert result == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    arr = []
    result = rotate_array_left(arr, 3)
    assert result == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    arr = [42]
    result = rotate_array_left(arr, 1)
    assert result == [42]

def test_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        rotate_array_left("not a list", 2)

def test_negative_rotation():
    """Test handling of negative rotation positions"""
    with pytest.raises(ValueError):
        rotate_array_left([1, 2, 3], -1)