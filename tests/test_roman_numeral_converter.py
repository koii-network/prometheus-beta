import pytest
from src.roman_numeral_converter import convert_to_roman

def test_convert_to_roman_zero():
    assert convert_to_roman(0) == ""

def test_convert_to_roman_single_digit():
    assert convert_to_roman(1) == "I"
    assert convert_to_roman(4) == "IV"
    assert convert_to_roman(5) == "V"
    assert convert_to_roman(9) == "IX"

def test_convert_to_roman_two_digits():
    assert convert_to_roman(10) == "X"
    assert convert_to_roman(14) == "XIV"
    assert convert_to_roman(40) == "XL"
    assert convert_to_roman(50) == "L"
    assert convert_to_roman(90) == "XC"

def test_convert_to_roman_three_digits():
    assert convert_to_roman(100) == "C"
    assert convert_to_roman(400) == "CD"
    assert convert_to_roman(500) == "D"
    assert convert_to_roman(900) == "CM"

def test_convert_to_roman_large_numbers():
    assert convert_to_roman(1000) == "M"
    assert convert_to_roman(1984) == "MCMLXXXIV"
    assert convert_to_roman(3999) == "MMMCMXCIX"

def test_convert_to_roman_invalid_input():
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(4000)

def test_convert_to_roman_type_error():
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman(3.14)