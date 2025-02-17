import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive():
    """Test set bit counting for positive numbers"""
    assert count_set_bits(7) == 3  # Binary: 111
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(0) == 0  # No set bits
    assert count_set_bits(1) == 1  # Binary: 1
    assert count_set_bits(16) == 1  # Binary: 10000

def test_count_set_bits_negative():
    """Test set bit counting for negative numbers"""
    assert count_set_bits(-7) == 3  # Absolute value of -7 is 7
    assert count_set_bits(-15) == 4  # Absolute value of -15 is 15

def test_count_set_bits_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)