import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic right rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_zero_rotation():
    """Test rotation of 0"""
    assert rotate_array([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of single-element array"""
    assert rotate_array([42], 10) == [42]

def test_invalid_input_type():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test non-integer rotation amount raises TypeError"""
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount raises ValueError"""
    with pytest.raises(ValueError):
        rotate_array([1, 2, 3], -1)