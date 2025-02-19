import pytest
from src.list_rotation import rotate_list

def test_rotate_list_basic():
    """Test basic rotation of a list"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_list_zero_rotation():
    """Test rotation with k = 0"""
    original = [1, 2, 3, 4, 5]
    assert rotate_list(original, 0) == original

def test_rotate_list_full_rotation():
    """Test rotation equal to list length"""
    original = [1, 2, 3, 4, 5]
    assert rotate_list(original, 5) == original

def test_rotate_list_empty():
    """Test rotation of an empty list"""
    assert rotate_list([], 3) == []

def test_rotate_list_oversized_rotation():
    """Test rotation larger than list length"""
    assert rotate_list([1, 2, 3], 7) == [2, 3, 1]

def test_rotate_list_invalid_type_list():
    """Test invalid input type for list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)

def test_rotate_list_invalid_type_k():
    """Test invalid input type for k"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "2")

def test_rotate_list_negative_k():
    """Test negative rotation amount"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_list([1, 2, 3], -1)