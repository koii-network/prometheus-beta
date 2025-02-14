import pytest
from src.array_rotation import rotate_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 5) == arr

def test_zero_rotation():
    """Test zero rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 0) == arr

def test_rotation_larger_than_length():
    """Test rotation amount larger than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    arr = []
    assert rotate_left(arr, 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    arr = [42]
    assert rotate_left(arr, 1) == [42]

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        rotate_left("not a list", 2)
    
    with pytest.raises(TypeError):
        rotate_left([1, 2, 3], "not an int")

def test_negative_rotation():
    """Test modulo rotation for negative rotation values"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, -2) == [3, 4, 5, 1, 2]