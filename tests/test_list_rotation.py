import pytest
from src.list_rotation import rotate_list

def test_basic_rotation():
    """Test basic list rotation"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_zero_rotation():
    """Test rotation by 0 should return original list"""
    original = [1, 2, 3]
    assert rotate_list(original, 0) == original
    assert rotate_list(original, 0) is not original  # Should be a copy

def test_full_rotation():
    """Test rotation equal to list length"""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation larger than list length"""
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]

def test_empty_list():
    """Test rotation of empty list"""
    assert rotate_list([], 5) == []

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "not an int")

def test_different_types_of_lists():
    """Test rotation works with different types of lists"""
    # Integer list
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    
    # Mixed type list
    mixed_list = [1, "a", True, None]
    assert rotate_list(mixed_list, 2) == [True, None, 1, "a"]

def test_list_copy():
    """Ensure the original list is not modified"""
    original = [1, 2, 3, 4, 5]
    rotated = rotate_list(original, 2)
    assert original == [1, 2, 3, 4, 5]  # Original should remain unchanged
    assert rotated == [4, 5, 1, 2, 3]   # Rotated list should be correct