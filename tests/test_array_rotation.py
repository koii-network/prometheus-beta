import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3], 5) == [2, 3, 1]

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of single-element array"""
    assert rotate_array([1], 1) == [1]

def test_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test invalid rotation type raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test that rotation works with negative indices mod array length"""
    assert rotate_array([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]