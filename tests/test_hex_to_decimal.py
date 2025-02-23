import pytest
from src.hex_to_decimal import hex_to_decimal

def test_basic_hex_conversion():
    """Test basic hexadecimal to decimal conversion."""
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('f') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('ff') == 255
    assert hex_to_decimal('100') == 256

def test_hex_with_prefix():
    """Test conversion with 0x or 0X prefix."""
    assert hex_to_decimal('0xa') == 10
    assert hex_to_decimal('0XFF') == 255

def test_mixed_case():
    """Test conversion with mixed case hex digits."""
    assert hex_to_decimal('Aa') == 170
    assert hex_to_decimal('fF') == 255

def test_large_hex_number():
    """Test conversion of larger hexadecimal numbers."""
    assert hex_to_decimal('1234') == 4660
    assert hex_to_decimal('abcdef') == 11259375

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        hex_to_decimal('')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('g')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('12345g')

def test_zero():
    """Test conversion of zero."""
    assert hex_to_decimal('0') == 0
    assert hex_to_decimal('00') == 0