import pytest
from src.array_rotation import rotate_array

def test_rotate_array_basic():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_array_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, len(arr)) == arr

def test_rotate_array_empty():
    """Test rotation of empty array"""
    assert rotate_array([], 3) == []

def test_rotate_array_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_rotate_array_large_rotation():
    """Test rotation amount larger than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_rotate_array_negative_error():
    """Test error handling for negative rotations"""
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], -1)

def test_rotate_array_type_errors():
    """Test type error handling"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)
    
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "not an int")