import pytest
from src.xor_array import xor_array_elements

def test_xor_array_normal_case():
    """Test XOR of a normal list of integers"""
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array_elements([5, 3, 2]) == 4  # 5 ^ 3 ^ 2 = 4

def test_xor_array_single_element():
    """Test XOR with a single element"""
    assert xor_array_elements([42]) == 42

def test_xor_array_large_numbers():
    """Test XOR with larger numbers"""
    assert xor_array_elements([1000, 2000, 3000]) == 3968  # actual bitwise XOR result

def test_xor_array_edge_cases():
    """Test various edge cases"""
    assert xor_array_elements([0, 0, 0]) == 0
    assert xor_array_elements([1, 1, 1]) == 1

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array_elements([-1, -2, -3]) == -4  # actual bitwise XOR result

def test_xor_array_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements("not a list")

def test_xor_array_non_integer_elements():
    """Test error handling for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1.5, 2, 3])

def test_xor_array_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])