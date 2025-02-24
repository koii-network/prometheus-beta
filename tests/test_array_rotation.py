import pytest
from src.array_rotation import rotate_left

def test_basic_rotation():
    """Test basic left rotation"""
    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotation_full_array():
    """Test rotation equal to array length"""
    assert rotate_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotation_more_than_length():
    """Test rotation more than array length"""
    assert rotate_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]

def test_zero_rotation():
    """Test zero rotation returns same array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_left(arr, 0) == arr
    assert rotate_left(arr, 0) is not arr  # Should be a new copy

def test_empty_array():
    """Test rotation on empty array"""
    assert rotate_left([], 3) == []

def test_single_element_array():
    """Test rotation on single element array"""
    assert rotate_left([42], 5) == [42]

def test_invalid_input_type():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_left("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_left([1, 2, 3], "2")

def test_negative_numbers_in_array():
    """Test rotation works with negative numbers"""
    assert rotate_left([-1, -2, -3, -4, -5], 2) == [-3, -4, -5, -1, -2]