import pytest
from src.hex_to_decimal import hex_to_decimal

def test_hex_to_decimal_basic():
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255

def test_hex_to_decimal_with_prefix():
    assert hex_to_decimal('0xA') == 10
    assert hex_to_decimal('0x10') == 16
    assert hex_to_decimal('0xFF') == 255

def test_hex_to_decimal_mixed_case():
    assert hex_to_decimal('Aa') == 170
    assert hex_to_decimal('0xAa') == 170

def test_hex_to_decimal_large_number():
    assert hex_to_decimal('1234') == 4660
    assert hex_to_decimal('0x1234') == 4660

def test_hex_to_decimal_invalid_input():
    with pytest.raises(ValueError):
        hex_to_decimal('G')
    with pytest.raises(ValueError):
        hex_to_decimal('xyz')
    with pytest.raises(ValueError):
        hex_to_decimal('')

def test_hex_to_decimal_zero():
    assert hex_to_decimal('0') == 0
    assert hex_to_decimal('0x0') == 0