import pytest
from src.hex_to_decimal import hex_to_decimal

def test_hex_to_decimal_basic_conversion():
    """Test basic hexadecimal to decimal conversions"""
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255
    assert hex_to_decimal('100') == 256

def test_hex_to_decimal_with_prefix():
    """Test conversions with '0x' prefix"""
    assert hex_to_decimal('0xA') == 10
    assert hex_to_decimal('0xff') == 255
    assert hex_to_decimal('0x100') == 256

def test_hex_to_decimal_mixed_case():
    """Test conversions with mixed case input"""
    assert hex_to_decimal('Aa') == 170
    assert hex_to_decimal('0xFf') == 255

def test_hex_to_decimal_large_number():
    """Test conversion of larger hexadecimal numbers"""
    assert hex_to_decimal('1A85') == 6789
    assert hex_to_decimal('0x1A85') == 6789

def test_hex_to_decimal_invalid_input():
    """Test that invalid hex strings raise ValueError"""
    with pytest.raises(ValueError):
        hex_to_decimal('G')
    with pytest.raises(ValueError):
        hex_to_decimal('1A85G')
    with pytest.raises(ValueError):
        hex_to_decimal('')