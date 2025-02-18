import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_single_digit():
    assert decimal_to_hex(9) == "9"
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"

def test_decimal_to_hex_multi_digit():
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"
    assert decimal_to_hex(4096) == "1000"

def test_decimal_to_hex_large_number():
    assert decimal_to_hex(1048575) == "FFFFF"

def test_decimal_to_hex_invalid_input_type():
    with pytest.raises(TypeError):
        decimal_to_hex("123")
    with pytest.raises(TypeError):
        decimal_to_hex(3.14)
    with pytest.raises(TypeError):
        decimal_to_hex(None)

def test_decimal_to_hex_negative_number():
    with pytest.raises(ValueError):
        decimal_to_hex(-10)