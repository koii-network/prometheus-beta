import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_zero():
    """Test that zero returns 0."""
    assert find_rightmost_set_bit(0) == 0

def test_powers_of_two():
    """Test positions for powers of 2."""
    assert find_rightmost_set_bit(1) == 1   # 2^0
    assert find_rightmost_set_bit(2) == 2   # 2^1
    assert find_rightmost_set_bit(4) == 3   # 2^2
    assert find_rightmost_set_bit(8) == 4   # 2^3
    assert find_rightmost_set_bit(16) == 5  # 2^4

def test_mixed_numbers():
    """Test numbers with multiple bits set."""
    assert find_rightmost_set_bit(3) == 1   # 11 in binary
    assert find_rightmost_set_bit(10) == 2  # 1010 in binary
    assert find_rightmost_set_bit(12) == 3  # 1100 in binary

def test_large_number():
    """Test a larger number."""
    assert find_rightmost_set_bit(1024) == 11  # 2^10

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    
    with pytest.raises(ValueError):
        find_rightmost_set_bit(-1)