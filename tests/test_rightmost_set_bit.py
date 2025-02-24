import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_positive_numbers():
    """Test various positive numbers."""
    assert find_rightmost_set_bit(18) == 2  # 10010 in binary
    assert find_rightmost_set_bit(16) == 5  # 10000 in binary
    assert find_rightmost_set_bit(7) == 1   # 111 in binary
    assert find_rightmost_set_bit(8) == 4   # 1000 in binary

def test_edge_cases():
    """Test edge cases."""
    assert find_rightmost_set_bit(0) == 0   # No set bits
    assert find_rightmost_set_bit(1) == 1   # Least significant bit

def test_large_numbers():
    """Test large numbers."""
    assert find_rightmost_set_bit(2**30) == 31  # Large power of 2
    assert find_rightmost_set_bit(2**63 - 1) == 1  # All ones

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    with pytest.raises(TypeError):
        find_rightmost_set_bit(None)