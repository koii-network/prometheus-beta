import pytest
from src.decimal_to_hex import decimal_to_hex

def test_zero_conversion():
    assert decimal_to_hex(0) == "0"

def test_small_decimal_conversions():
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"

def test_larger_decimal_conversions():
    assert decimal_to_hex(4096) == "1000"
    assert decimal_to_hex(1000000) == "F4240"

def test_invalid_input_types():
    with pytest.raises(TypeError):
        decimal_to_hex("123")
    with pytest.raises(TypeError):
        decimal_to_hex(3.14)
    with pytest.raises(TypeError):
        decimal_to_hex(None)

def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_hex(-10)