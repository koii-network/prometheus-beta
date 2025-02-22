import pytest
from src.list_rotation import rotate_list

def test_basic_rotation():
    """Test basic list rotation"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to list length"""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_partial_rotation():
    """Test rotation less than list length"""
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]

def test_empty_list():
    """Test rotation of an empty list"""
    assert rotate_list([], 5) == []

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_large_rotation():
    """Test rotation larger than list length"""
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]

def test_negative_large_rotation():
    """Test rotation larger than list length"""
    assert rotate_list([1, 2, 3], 10) == [2, 3, 1]

def test_invalid_input_non_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)

def test_invalid_input_non_integer_k():
    """Test that non-integer k raises TypeError"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "2")