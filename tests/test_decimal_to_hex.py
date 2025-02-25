import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_basic():
    """Test basic decimal to hex conversions"""
    assert decimal_to_hex(0) == "0"
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"
    assert decimal_to_hex(4096) == "1000"

def test_decimal_to_hex_large_number():
    """Test conversion of large decimal numbers"""
    assert decimal_to_hex(1000000) == "F4240"

def test_decimal_to_hex_error_handling():
    """Test error handling for invalid inputs"""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("100")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(None)