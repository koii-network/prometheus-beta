import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotation_full_array():
    """Test rotation equal to array length"""
    assert rotate_array_left([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_more_than_length():
    """Test rotation more than array length"""
    assert rotate_array_left([1, 2, 3], 5) == [3, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array_left([], 3) == []

def test_zero_rotation():
    """Test rotation by zero positions"""
    assert rotate_array_left([1, 2, 3], 0) == [1, 2, 3]

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_invalid_input_non_integer_rotation():
    """Test raising TypeError for non-integer rotation"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test raising ValueError for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)