import pytest
from src.array_xor import xor_array_elements

def test_xor_array_elements_basic():
    """Test XOR with a basic list of integers"""
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array_elements([5, 3, 1]) == 7  # 5 ^ 3 ^ 1 = 7

def test_xor_array_single_element():
    """Test XOR with a single element list"""
    assert xor_array_elements([42]) == 42

def test_xor_array_all_zeros():
    """Test XOR with all zero elements"""
    assert xor_array_elements([0, 0, 0]) == 0

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array_elements([-1, -2, -3]) == 0

def test_xor_array_empty_list():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])

def test_xor_array_non_list_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements(42)

def test_xor_array_non_integer_elements():
    """Test that list with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, "3"])
        xor_array_elements([1.5, 2, 3])
        xor_array_elements([True, False])