import pytest
from src.hex_to_decimal import hex_to_decimal

def test_basic_hex_conversion():
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255

def test_hex_with_prefix():
    assert hex_to_decimal('0x1A') == 26
    assert hex_to_decimal('0XFF') == 255

def test_mixed_case_hex():
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('Ff') == 255

def test_invalid_hex_input():
    with pytest.raises(ValueError):
        hex_to_decimal('G')
    
    with pytest.raises(ValueError):
        hex_to_decimal('123xyz')

def test_zero_conversion():
    assert hex_to_decimal('0') == 0
    assert hex_to_decimal('00') == 0

def test_large_hex_number():
    assert hex_to_decimal('1234ABCD') == 305419905
    assert hex_to_decimal('0xFFFFFFFF') == 4294967295