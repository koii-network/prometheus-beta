import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_partial_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 3) == [4, 5, 1, 2, 3]

def test_zero_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_empty_array():
    arr = []
    assert rotate_array_left(arr, 2) == []

def test_rotation_larger_than_array():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_invalid_rotation_type():
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)