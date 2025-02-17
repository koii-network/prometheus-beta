import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive_numbers():
    """Test count_set_bits with various positive numbers."""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(7) == 3     # 111 in binary
    assert count_set_bits(15) == 4    # 1111 in binary
    assert count_set_bits(16) == 1    # 10000 in binary
    assert count_set_bits(255) == 8   # 11111111 in binary

def test_count_set_bits_negative_numbers():
    """Test count_set_bits with negative numbers."""
    assert count_set_bits(-1) == 64   # All 64 bits set in two's complement
    assert count_set_bits(-7) == 61   # 64 bits minus the 3 bits in positive 7
    assert count_set_bits(-15) == 60  # 64 bits minus the 4 bits in positive 15

def test_count_set_bits_large_numbers():
    """Test count_set_bits with large numbers."""
    large_num = 2**30 - 1
    assert count_set_bits(large_num) == 30

def test_count_set_bits_zero():
    """Test that zero returns zero set bits."""
    assert count_set_bits(0) == 0

def test_count_set_bits_power_of_two():
    """Test numbers that are powers of two."""
    assert count_set_bits(2**0) == 1   # 1
    assert count_set_bits(2**1) == 1   # 2
    assert count_set_bits(2**10) == 1  # 1024
    assert count_set_bits(2**31) == 1  # Large power of two