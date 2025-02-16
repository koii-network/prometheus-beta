import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array([], 3) == []

def test_zero_rotation():
    """Test rotation by zero positions"""
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation more than array length"""
    assert rotate_array([1, 2, 3], 5) == [2, 3, 1]

def test_single_element_array():
    """Test rotation of a single element array"""
    assert rotate_array([42], 1) == [42]

def test_invalid_input_type():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test non-integer rotation raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation raises ValueError"""
    with pytest.raises(ValueError):
        rotate_array([1, 2, 3], -1)