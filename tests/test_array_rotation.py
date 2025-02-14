import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic right rotation of an array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 5) == arr

def test_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_empty_array():
    """Test rotation of an empty array"""
    arr = []
    assert rotate_array(arr, 3) == []

def test_large_rotation():
    """Test rotation larger than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 7) == [4, 5, 1, 2, 3]

def test_single_element_array():
    """Test rotation of a single-element array"""
    arr = [42]
    assert rotate_array(arr, 1) == [42]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test that TypeError is raised for non-integer rotation"""
    with pytest.raises(TypeError, match="Rotation positions must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test that ValueError is raised for negative rotation"""
    with pytest.raises(ValueError, match="Rotation positions cannot be negative"):
        rotate_array([1, 2, 3], -1)