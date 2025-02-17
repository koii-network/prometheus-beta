import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_find_rightmost_set_bit_basic():
    assert find_rightmost_set_bit(10) == 2  # Binary: 1010, rightmost set bit is at position 2
    assert find_rightmost_set_bit(7) == 1   # Binary: 111, rightmost set bit is at position 1
    assert find_rightmost_set_bit(16) == 5  # Binary: 10000, rightmost set bit is at position 5

def test_find_rightmost_set_bit_edge_cases():
    assert find_rightmost_set_bit(0) == 0   # No set bits
    assert find_rightmost_set_bit(1) == 1   # Smallest set bit
    assert find_rightmost_set_bit(128) == 8 # A higher power of 2

def test_find_rightmost_set_bit_invalid_inputs():
    with pytest.raises(TypeError):
        find_rightmost_set_bit("10")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    
    with pytest.raises(ValueError):
        find_rightmost_set_bit(-5)