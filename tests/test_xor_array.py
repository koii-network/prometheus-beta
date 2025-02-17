import pytest
from src.xor_array import xor_array

def test_xor_array_basic():
    """Test basic XOR operation with multiple integers"""
    assert xor_array([1, 2, 3]) == 0  # 1 XOR 2 XOR 3 = 0
    assert xor_array([5, 7, 2]) == 0  # 5 XOR 7 XOR 2 = 0

def test_xor_array_single_element():
    """Test XOR with a single element"""
    assert xor_array([42]) == 42

def test_xor_array_large_numbers():
    """Test XOR with larger numbers"""
    assert xor_array([100, 200, 300]) == 260

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array([-1, -2, -3]) == 0

def test_xor_array_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array(42)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array([1, 2, "3"])
    
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array([])