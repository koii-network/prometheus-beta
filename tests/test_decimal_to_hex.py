import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    """Test conversion of zero."""
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_small_numbers():
    """Test conversion of small positive integers."""
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"

def test_decimal_to_hex_larger_numbers():
    """Test conversion of larger numbers."""
    assert decimal_to_hex(4096) == "1000"
    assert decimal_to_hex(65535) == "FFFF"

def test_decimal_to_hex_error_negative():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-1)

def test_decimal_to_hex_error_non_integer():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("100")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(None)