import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive():
    assert count_set_bits(7) == 3  # 111 in binary
    assert count_set_bits(15) == 4  # 1111 in binary
    assert count_set_bits(0) == 0  # No set bits
    assert count_set_bits(1) == 1  # Single bit

def test_count_set_bits_negative():
    assert count_set_bits(-7) == 3  # Absolute value of -7
    assert count_set_bits(-15) == 4  # Absolute value of -15

def test_count_set_bits_large_number():
    assert count_set_bits(2**10 - 1) == 10  # 1023, all 10 bits set
    assert count_set_bits(2**20 - 1) == 20  # Large number with 20 set bits

def test_count_set_bits_error_handling():
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)