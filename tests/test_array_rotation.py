import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 2)
    assert result == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length (no change)"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 5)
    assert result == [1, 2, 3, 4, 5]

def test_zero_rotation():
    """Test rotation of 0 positions"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 0)
    assert result == [1, 2, 3, 4, 5]

def test_large_rotation():
    """Test rotation larger than array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 7)
    assert result == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    arr = []
    result = rotate_array_left(arr, 2)
    assert result == []

def test_single_element_array():
    """Test rotation of single element array"""
    arr = [42]
    result = rotate_array_left(arr, 1)
    assert result == [42]

def test_type_error_non_list():
    """Test type error when input is not a list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_type_error_non_integer_rotation():
    """Test type error when rotation amount is not an integer"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_value_error_negative_rotation():
    """Test value error when rotation amount is negative"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)