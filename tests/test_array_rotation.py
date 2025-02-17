import pytest
from src.array_rotation import rotate_array_left

def test_rotate_array_left_basic():
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotate_array_left_zero_rotation():
    assert rotate_array_left([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

def test_rotate_array_left_full_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, len(arr)) == arr

def test_rotate_array_left_empty_array():
    assert rotate_array_left([], 3) == []

def test_rotate_array_left_large_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_rotate_array_left_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_rotate_array_left_invalid_rotation_type():
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_rotate_array_left_negative_rotation():
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)