import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_case():
    """Test reversing a standard 32-bit number."""
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_all_ones():
    """Test when all bits are 1."""
    assert reverse_bits(4294967295) == 4294967295

def test_reverse_bits_zero():
    """Test reversing zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_small_number():
    """Test reversing a small number."""
    assert reverse_bits(1) == 2147483648  # 1 becomes 2^31

def test_reverse_bits_power_of_two():
    """Test reversing a power of two."""
    assert reverse_bits(16) == 268435456  # 2^4 becomes 2^28

def test_reverse_bits_multiple_edge_cases():
    """Test multiple edge cases."""
    test_cases = [
        (0, 0),
        (1, 2147483648),
        (4294967295, 4294967295),
        (16, 268435456),
        (43261596, 964176192)
    ]
    
    for input_num, expected_output in test_cases:
        assert reverse_bits(input_num) == expected_output