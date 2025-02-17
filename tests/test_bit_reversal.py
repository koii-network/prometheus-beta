import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_case():
    # Test case from the function docstring
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    # Test reversing zero
    assert reverse_bits(0) == 0

def test_reverse_bits_all_ones():
    # Test reversing a number with all bits set
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_power_of_two():
    # Test reversing a power of two
    assert reverse_bits(1) == 2147483648  # 1 reversed is 2^31

def test_reverse_bits_random_numbers():
    # Test a few random numbers
    test_cases = [
        (123456, 1343619072),
        (987654, 1275068160),
        (2**30, 2)
    ]
    for input_num, expected in test_cases:
        assert reverse_bits(input_num) == expected

def test_reverse_bits_input_range():
    # Ensure the function handles 32-bit unsigned integer range
    max_32bit = 0xFFFFFFFF
    assert 0 <= reverse_bits(max_32bit) <= max_32bit
    assert 0 <= reverse_bits(0) <= max_32bit