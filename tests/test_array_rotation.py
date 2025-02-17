import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotation_full_length():
    assert rotate_array_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotation_multiple_full_lengths():
    assert rotate_array_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    assert rotate_array_left([], 3) == []

def test_no_rotation():
    assert rotate_array_left([1, 2, 3], 0) == [1, 2, 3]

def test_single_element_array():
    assert rotate_array_left([42], 1) == [42]

def test_invalid_input_types():
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation count must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    with pytest.raises(ValueError, match="Rotation count cannot be negative"):
        rotate_array_left([1, 2, 3], -1)