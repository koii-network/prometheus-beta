import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_basic():
    # A sample input to test
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    # Test with zero
    assert reverse_bits(0) == 0

def test_reverse_bits_max_32bit():
    # Test with maximum 32-bit unsigned integer
    max_32bit = 0xFFFFFFFF
    assert reverse_bits(max_32bit) == max_32bit

def test_reverse_bits_powers_of_two():
    # Test with powers of two
    assert reverse_bits(1) == 2147483648  # 2^31
    assert reverse_bits(2) == 1073741824  # 2^30
    assert reverse_bits(4) == 536870912   # 2^29

def test_reverse_bits_boundary_conditions():
    # Test edge cases and boundary conditions
    test_cases = [
        (0x55555555, 0xAAAAAAAA),  # Alternating bit pattern
        (0xAAAAAAAA, 0x55555555),  # Opposite alternating bit pattern
        (1, 2**31),                # Minimum non-zero number
        (2**31, 1)                 # Largest bit on
    ]
    
    for input_val, expected in test_cases:
        assert reverse_bits(input_val) == expected