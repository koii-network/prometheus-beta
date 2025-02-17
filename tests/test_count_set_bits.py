import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive_numbers():
    assert count_set_bits(7) == 3    # Binary: 111
    assert count_set_bits(15) == 4   # Binary: 1111
    assert count_set_bits(0) == 0    # Binary: 0
    assert count_set_bits(1) == 1    # Binary: 1
    assert count_set_bits(16) == 1   # Binary: 10000

def test_count_set_bits_negative_numbers():
    assert count_set_bits(-7) == 3   # Absolute value: 7, Binary: 111
    assert count_set_bits(-15) == 4  # Absolute value: 15, Binary: 1111

def test_count_set_bits_large_numbers():
    assert count_set_bits(2**10 - 1) == 10  # 1023 = 2^10 - 1
    assert count_set_bits(2**20 - 1) == 20  # 1048575 = 2^20 - 1

def test_count_set_bits_invalid_input():
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)