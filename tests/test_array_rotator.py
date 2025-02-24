import pytest
from src.array_rotator import rotate_array

def test_basic_rotation():
    """Test basic right rotation of an array"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation by full array length"""
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_zero_rotation():
    """Test rotation by zero positions"""
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3], 5) == [2, 3, 1]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array([42], 10) == [42]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test that TypeError is raised for non-integer rotation"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test that ValueError is raised for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)