import pytest
from src.hex_to_decimal import hex_to_decimal

def test_basic_hex_conversion():
    """Test basic hexadecimal to decimal conversions."""
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255
    assert hex_to_decimal('100') == 256

def test_hex_with_prefix():
    """Test hexadecimal strings with '0x' or '0X' prefix."""
    assert hex_to_decimal('0x10') == 16
    assert hex_to_decimal('0X1A') == 26

def test_case_insensitivity():
    """Test that conversion works with both uppercase and lowercase."""
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('Ff') == 255

def test_large_hex_number():
    """Test conversion of larger hexadecimal numbers."""
    assert hex_to_decimal('1234') == 4660
    assert hex_to_decimal('ABCDEF') == 11259375

def test_invalid_hex_input():
    """Test that invalid hexadecimal inputs raise ValueError."""
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('G')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('12.34')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('')

def test_zero_hex():
    """Test conversion of zero."""
    assert hex_to_decimal('0') == 0
    assert hex_to_decimal('00') == 0
    assert hex_to_decimal('0x0') == 0