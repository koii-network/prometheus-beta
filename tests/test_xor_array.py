import pytest
from src.xor_array import xor_array

def test_xor_array_normal():
    """Test XOR with a normal list of integers"""
    assert xor_array([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array([4, 5, 6]) == 7  # 4 ^ 5 ^ 6 = 7

def test_xor_array_single_element():
    """Test XOR with a single-element list"""
    assert xor_array([42]) == 42

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array([-1, -2, -3]) == 0

def test_xor_array_zero():
    """Test XOR with lists containing zero"""
    assert xor_array([0, 1, 2]) == 3
    assert xor_array([0, 0, 0]) == 0

def test_xor_array_error_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array([])

def test_xor_array_error_non_list():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array("not a list")

def test_xor_array_error_non_integer():
    """Test that lists with non-integer elements raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array([1.5, 2, 3])