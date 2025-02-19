import pytest
from src.list_rotation import rotate_list

def test_rotate_list_basic():
    """Test basic list rotation"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_list_full_rotation():
    """Test rotation equal to list length (no change)"""
    test_list = [1, 2, 3, 4, 5]
    assert rotate_list(test_list, 5) == test_list

def test_rotate_list_empty():
    """Test rotation of empty list"""
    assert rotate_list([], 3) == []

def test_rotate_list_no_rotation():
    """Test list with zero rotation"""
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_rotate_list_multiple_rotations():
    """Test rotations greater than list length"""
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_rotate_list_negative_input():
    """Test input validation for negative rotation"""
    with pytest.raises(TypeError):
        rotate_list([1, 2, 3], -2)

def test_rotate_list_invalid_input_type():
    """Test input validation for invalid list type"""
    with pytest.raises(TypeError):
        rotate_list("not a list", 2)
    with pytest.raises(TypeError):
        rotate_list([1, 2, 3], "not an integer")