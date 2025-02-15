import pytest
from src.bit_counter import count_set_bits

def test_count_set_bits_zero():
    """Test counting set bits for zero."""
    assert count_set_bits(0) == 0

def test_count_set_bits_positive():
    """Test counting set bits for positive integers."""
    assert count_set_bits(5) == 2  # 101 in binary
    assert count_set_bits(7) == 3  # 111 in binary
    assert count_set_bits(15) == 4  # 1111 in binary

def test_count_set_bits_negative():
    """Test counting set bits for negative integers."""
    assert count_set_bits(-5) == 2  # Absolute value of 5
    assert count_set_bits(-15) == 4  # Absolute value of 15

def test_count_set_bits_large_number():
    """Test counting set bits for a large number."""
    assert count_set_bits(2**10 - 1) == 10  # 1023 in decimal, all 10 bits set

def test_count_set_bits_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)