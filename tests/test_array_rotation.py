import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic right rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 2) == [4, 5, 1, 2, 3]

def test_zero_rotation():
    """Test when rotation amount is zero"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 5) == arr

def test_over_rotation():
    """Test rotation more than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 7) == [4, 5, 1, 2, 3]

def test_empty_array():
    """Test rotation of an empty array"""
    arr = []
    assert rotate_array(arr, 3) == []

def test_invalid_input_types():
    """Test raising TypeError for invalid input types"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)
    
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "not an int")

def test_single_element_array():
    """Test rotation of a single-element array"""
    arr = [42]
    assert rotate_array(arr, 3) == [42]