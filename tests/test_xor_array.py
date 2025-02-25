import pytest
from src.xor_array import xor_array

def test_xor_array_basic():
    """Test basic XOR array calculation"""
    assert xor_array([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array([5, 3, 2]) == 4  # 5 ^ 3 ^ 2 = 4

def test_xor_array_single_element():
    """Test XOR with a single element"""
    assert xor_array([42]) == 42

def test_xor_array_large_numbers():
    """Test XOR with larger numbers"""
    assert xor_array([1000, 2000, 3000]) == 0

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array([-1, -2, -3]) == 0

def test_xor_array_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array("not a list")
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array([1, 2, "three"])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array([1, 2, 3.14])

def test_xor_array_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array([])