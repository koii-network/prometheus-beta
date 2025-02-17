import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, len(arr)) == arr

def test_empty_array():
    assert rotate_array([], 3) == []

def test_zero_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_rotation_larger_than_length():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 7) == [4, 5, 1, 2, 3]

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    with pytest.raises(TypeError, match="Rotation count must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_single_element_array():
    assert rotate_array([42], 1) == [42]