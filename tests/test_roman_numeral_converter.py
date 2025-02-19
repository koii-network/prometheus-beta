import pytest
from src.roman_numeral_converter import int_to_roman

def test_int_to_roman_zero():
    assert int_to_roman(0) == ""

def test_int_to_roman_basic_numbers():
    assert int_to_roman(1) == "I"
    assert int_to_roman(5) == "V"
    assert int_to_roman(10) == "X"
    assert int_to_roman(50) == "L"
    assert int_to_roman(100) == "C"
    assert int_to_roman(500) == "D"
    assert int_to_roman(1000) == "M"

def test_int_to_roman_compound_numbers():
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(90) == "XC"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(900) == "CM"

def test_int_to_roman_larger_numbers():
    assert int_to_roman(3999) == "MMMCMXCIX"
    assert int_to_roman(2023) == "MMXXIII"
    assert int_to_roman(1984) == "MCMLXXXIV"

def test_int_to_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_roman(-1)
    
    with pytest.raises(ValueError):
        int_to_roman(4000)

def test_int_to_roman_type_error():
    with pytest.raises(TypeError):
        int_to_roman("123")
    
    with pytest.raises(TypeError):
        int_to_roman(3.14)