import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_small_numbers():
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"

def test_decimal_to_hex_larger_numbers():
    assert decimal_to_hex(4096) == "1000"
    assert decimal_to_hex(65535) == "FFFF"
    assert decimal_to_hex(1048575) == "FFFFF"

def test_decimal_to_hex_negative_input():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-1)

def test_decimal_to_hex_invalid_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(None)