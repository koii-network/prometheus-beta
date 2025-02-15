import pytest
from src.bit_operations import count_set_bits

def test_count_set_bits_positive_numbers():
    assert count_set_bits(7) == 3  # Binary: 111
    assert count_set_bits(16) == 1  # Binary: 10000
    assert count_set_bits(15) == 4  # Binary: 1111

def test_count_set_bits_zero():
    assert count_set_bits(0) == 0

def test_count_set_bits_large_number():
    assert count_set_bits(2**10 - 1) == 10  # 1023 in decimal
    assert count_set_bits(2**20 - 1) == 20

def test_count_set_bits_negative_numbers():
    assert count_set_bits(-7) == 3
    assert count_set_bits(-16) == 1

def test_count_set_bits_single_bit():
    assert count_set_bits(1) == 1
    assert count_set_bits(2) == 1
    assert count_set_bits(4) == 1
    assert count_set_bits(8) == 1