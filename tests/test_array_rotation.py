import pytest
from src.array_rotation import rotate_array

def test_rotate_array_basic():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_array_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_rotate_array_full_rotation():
    """Test rotation by full array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 5) == arr

def test_rotate_array_empty():
    """Test rotation of empty array"""
    assert rotate_array([], 3) == []

def test_rotate_array_large_rotation():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_rotate_array_negative_input():
    """Test negative rotation raises ValueError"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)

def test_rotate_array_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_rotate_array_preserves_original():
    """Ensure original array is not modified"""
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 2)
    assert arr == [1, 2, 3, 4, 5]