import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_known_value():
    """Test reversal of a known input value."""
    # Input:  00000010100101000001111010011100
    # Output: 00111001011110000010100101000000
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    """Test bit reversal of zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_all_ones():
    """Test bit reversal of all 1s."""
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_symmetric_examples():
    """Test several symmetric bit reversal cases."""
    test_cases = [
        0x12345678,  # A random 32-bit number
        0xA5A5A5A5,  # Alternating bit pattern
        0x80000001,  # Most and least significant bit set
    ]
    
    for num in test_cases:
        # Reversing twice should return the original number
        assert reverse_bits(reverse_bits(num)) == num

def test_reverse_bits_input_range():
    """Ensure function works with 32-bit unsigned integer range."""
    max_32bit = 0xFFFFFFFF
    min_32bit = 0
    
    assert 0 <= reverse_bits(min_32bit) <= max_32bit
    assert 0 <= reverse_bits(max_32bit) <= max_32bit