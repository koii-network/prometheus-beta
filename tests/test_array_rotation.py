import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    # Test basic left rotation
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    # Test rotation equal to array length (should return original array)
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_zero_rotation():
    # Test zero rotation
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_empty_array():
    # Test empty array
    assert rotate_array_left([], 3) == []

def test_rotation_larger_than_array():
    # Test rotation larger than array length
    arr = [1, 2, 3]
    assert rotate_array_left(arr, 5) == [2, 3, 1]

def test_type_error_invalid_array():
    # Test type error for non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_type_error_invalid_rotation():
    # Test type error for non-integer rotation
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_value_error_negative_rotation():
    # Test value error for negative rotation
    with pytest.raises(ValueError, match="Rotation amount must be non-negative"):
        rotate_array_left([1, 2, 3], -1)