import pytest
from src.array_rotator import rotate_array

def test_basic_rotation():
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotation_full_cycle():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, len(arr)) == arr

def test_rotation_zero():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_rotation_longer_than_array():
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 7) == [4, 5, 1, 2, 3]

def test_empty_array():
    assert rotate_array([], 3) == []

def test_single_element_array():
    assert rotate_array([42], 5) == [42]

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")