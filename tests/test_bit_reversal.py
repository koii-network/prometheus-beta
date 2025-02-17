import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_example_case():
    """Test the example case provided in the function docstring."""
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_all_ones():
    """Test reversing a number with all bits set to 1."""
    assert reverse_bits(4294967295) == 4294967295

def test_reverse_bits_zero():
    """Test reversing zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_power_of_two():
    """Test reversing a power of two."""
    assert reverse_bits(1) == 2147483648  # 1 -> 10000000000000000000000000000000

def test_reverse_bits_mixed_bits():
    """Test reversing a number with mixed bit pattern."""
    assert reverse_bits(123456) == 1260454400

def test_reverse_bits_large_number():
    """Test reversing a larger number."""
    assert reverse_bits(2**31) == 2

def test_input_type_validation():
    """Ensure the function handles invalid input types."""
    with pytest.raises(TypeError):
        reverse_bits("not an integer")
    with pytest.raises(TypeError):
        reverse_bits(3.14)