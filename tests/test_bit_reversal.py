import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_case():
    """Test a standard case of bit reversal."""
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    """Test bit reversal for zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_all_ones():
    """Test bit reversal for all ones (max 32-bit unsigned int)."""
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_power_of_two():
    """Test bit reversal for a power of two."""
    assert reverse_bits(1) == 2147483648  # 1 becomes 2^31

def test_reverse_bits_invalid_input_negative():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(-1)

def test_reverse_bits_invalid_input_too_large():
    """Test that inputs larger than 32-bit unsigned int raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(0x100000000)

def test_reverse_bits_invalid_input_non_integer():
    """Test that non-integer inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits("not an integer")