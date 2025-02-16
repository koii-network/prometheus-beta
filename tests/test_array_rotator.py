import pytest
from src.array_rotator import rotate_left

def test_rotate_left_basic():
    # Basic rotation
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotate_left_zero():
    # Zero rotation should return original array
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 0) == arr

def test_rotate_left_full_rotation():
    # Rotation equal to array length should return original array
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 5) == arr

def test_rotate_left_over_rotation():
    # Rotation more than array length should wrap around
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 7) == [3, 4, 5, 1, 2]

def test_rotate_left_empty_array():
    # Empty array should return empty array
    arr = []
    assert rotate_left(arr, 3) == []

def test_rotate_left_type_error():
    # Non-list input should raise TypeError
    with pytest.raises(TypeError):
        rotate_left("not a list", 2)
    with pytest.raises(TypeError):
        rotate_left([1, 2, 3], "2")

def test_rotate_left_negative_rotation():
    # Negative rotation should raise ValueError
    with pytest.raises(ValueError):
        rotate_left([1, 2, 3], -1)