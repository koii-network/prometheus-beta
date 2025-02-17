import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive():
    """Test counting set bits for positive integers"""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(7) == 3    # 111 in binary
    assert count_set_bits(10) == 2   # 1010 in binary
    assert count_set_bits(15) == 4   # 1111 in binary

def test_count_set_bits_negative():
    """Test counting set bits for negative integers"""
    assert count_set_bits(-1) == 64  # All 64 bits set for 2's complement
    assert count_set_bits(-7) == 61  # Negative number handling
    
def test_count_set_bits_large_number():
    """Test with larger numbers"""
    assert count_set_bits(2**10 - 1) == 10  # 1023, with 10 set bits
    assert count_set_bits(2**20 - 1) == 20  # 1048575, with 20 set bits

def test_count_set_bits_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)