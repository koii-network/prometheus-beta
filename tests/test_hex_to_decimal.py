import pytest
from src.hex_to_decimal import hex_to_decimal

def test_valid_hex_conversion():
    # Test basic conversions
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255
    assert hex_to_decimal('100') == 256

def test_hex_with_prefix():
    # Test conversions with '0x' or '0X' prefix
    assert hex_to_decimal('0xA') == 10
    assert hex_to_decimal('0XFF') == 255

def test_mixed_case_hex():
    # Test conversion with mixed case
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('Ff') == 255

def test_long_hex_number():
    # Test longer hexadecimal numbers
    assert hex_to_decimal('1A2B3C') == 1717052

def test_invalid_hex_input():
    # Test invalid hexadecimal inputs
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('G')
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('123Z')
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('')