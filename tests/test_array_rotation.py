import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    # Test basic right rotation
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    # Rotating by length of array should return the same array
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_zero_rotation():
    # Rotating by 0 should return a copy of the original array
    original = [1, 2, 3]
    result = rotate_array(original, 0)
    assert result == original
    assert result is not original

def test_rotation_larger_than_length():
    # Rotation larger than array length should wrap around
    assert rotate_array([1, 2, 3], 4) == [3, 1, 2]

def test_empty_array():
    # Empty array should remain empty
    assert rotate_array([], 5) == []

def test_single_element_array():
    # Single element array should remain unchanged
    assert rotate_array([42], 10) == [42]

def test_invalid_input_types():
    # Test type validation
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    # Test negative rotation handling
    with pytest.raises(ValueError, match="Rotation amount must be non-negative"):
        rotate_array([1, 2, 3], -1)