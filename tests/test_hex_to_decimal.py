import pytest
from src.hex_to_decimal import hex_to_decimal

def test_hex_to_decimal_basic():
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255

def test_hex_to_decimal_with_prefix():
    assert hex_to_decimal('0x10') == 16
    assert hex_to_decimal('0XFF') == 255

def test_hex_to_decimal_mixed_case():
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('Ff') == 255

def test_hex_to_decimal_large_number():
    assert hex_to_decimal('1A5') == 421
    assert hex_to_decimal('0xABC123') == 11256099

def test_hex_to_decimal_invalid_input():
    with pytest.raises(ValueError):
        hex_to_decimal('G')
    
    with pytest.raises(ValueError):
        hex_to_decimal('12345z')
    
    with pytest.raises(ValueError):
        hex_to_decimal('')