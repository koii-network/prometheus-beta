import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_find_rightmost_set_bit():
    # Test basic cases
    assert find_rightmost_set_bit(0) == 0  # No set bit
    assert find_rightmost_set_bit(1) == 1  # Rightmost bit at first position
    assert find_rightmost_set_bit(16) == 5  # Binary: 10000
    assert find_rightmost_set_bit(18) == 2  # Binary: 10010
    assert find_rightmost_set_bit(7) == 1   # Binary: 111
    assert find_rightmost_set_bit(8) == 4   # Binary: 1000
    assert find_rightmost_set_bit(64) == 7  # Binary: 1000000

def test_find_rightmost_set_bit_error_handling():
    # Test error handling
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    
    with pytest.raises(ValueError):
        find_rightmost_set_bit(-5)

def test_large_numbers():
    # Test large numbers
    assert find_rightmost_set_bit(2**30) == 31
    assert find_rightmost_set_bit(2**63) == 64  # Assuming 64-bit integer