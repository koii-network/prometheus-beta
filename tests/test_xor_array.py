import pytest
from src.xor_array import xor_array_elements

def test_xor_array_normal_case():
    """Test XOR of a normal array of integers."""
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array_elements([5, 7, 2]) == 0  # 5 ^ 7 ^ 2 = 0

def test_xor_array_single_element():
    """Test XOR with a single element array."""
    assert xor_array_elements([42]) == 42

def test_xor_array_large_numbers():
    """Test XOR with larger numbers."""
    assert xor_array_elements([1000, 2000, 3000]) == 3968

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers."""
    assert xor_array_elements([-1, -2, -3]) == -4

def test_xor_array_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        xor_array_elements("not a list")
    
    with pytest.raises(TypeError):
        xor_array_elements(123)

def test_xor_array_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError):
        xor_array_elements([])