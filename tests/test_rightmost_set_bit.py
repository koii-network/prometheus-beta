import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_find_rightmost_set_bit():
    # Test basic cases
    assert find_rightmost_set_bit(0) == 0    # No set bits
    assert find_rightmost_set_bit(1) == 1    # Least significant bit
    assert find_rightmost_set_bit(2) == 2    # Second bit from right
    assert find_rightmost_set_bit(3) == 1    # First bit from right in 3 (binary 11)
    assert find_rightmost_set_bit(8) == 4    # Fourth bit from right in 8 (binary 1000)
    assert find_rightmost_set_bit(16) == 5   # Fifth bit from right in 16 (binary 10000)

def test_large_numbers():
    assert find_rightmost_set_bit(1024) == 11  # 2^10
    assert find_rightmost_set_bit(2**30) == 31  # Large power of 2

def test_invalid_input():
    # Test error handling
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    with pytest.raises(TypeError):
        find_rightmost_set_bit(None)