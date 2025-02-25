import pytest
from src.list_rotation import rotate_list

def test_rotate_list_basic():
    """Test basic list rotation"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_list_zero():
    """Test rotation by zero positions"""
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_rotate_list_full_rotation():
    """Test rotation equal to list length"""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_rotate_list_empty():
    """Test rotation of an empty list"""
    assert rotate_list([], 5) == []

def test_rotate_list_large_k():
    """Test rotation with k larger than list length"""
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]

def test_rotate_list_type_error_list():
    """Test type error when input is not a list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)

def test_rotate_list_type_error_k():
    """Test type error when k is not an integer"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "2")

def test_rotate_list_negative_k():
    """Test value error when k is negative"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_list([1, 2, 3], -1)