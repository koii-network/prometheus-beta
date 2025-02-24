import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_known_value():
    """Test reverse_bits with a known input and expected output."""
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_all_ones():
    """Test reverse_bits with all 1s (maximum 32-bit unsigned integer)."""
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_zero():
    """Test reverse_bits with zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_single_bit():
    """Test reverse_bits with a single bit set."""
    assert reverse_bits(1) == 2147483648  # 1 at first bit becomes 1 at last bit

def test_reverse_bits_invalid_input_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError):
        reverse_bits(-1)

def test_reverse_bits_invalid_input_too_large():
    """Test that an integer larger than 32-bit unsigned max raises a ValueError."""
    with pytest.raises(ValueError):
        reverse_bits(0x100000000)

def test_reverse_bits_invalid_input_type():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError):
        reverse_bits("not an integer")