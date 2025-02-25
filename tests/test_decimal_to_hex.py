import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    """Test conversion of zero"""
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_positive_numbers():
    """Test conversion of various positive decimal numbers"""
    test_cases = [
        (10, "A"),
        (15, "F"),
        (16, "10"),
        (255, "FF"),
        (4096, "1000")
    ]
    for decimal, expected in test_cases:
        assert decimal_to_hex(decimal) == expected

def test_decimal_to_hex_large_number():
    """Test conversion of a large decimal number"""
    assert decimal_to_hex(1000000) == "F4240"

def test_decimal_to_hex_invalid_type():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("100")
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(None)

def test_decimal_to_hex_negative_number():
    """Test that ValueError is raised for negative inputs"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-10)