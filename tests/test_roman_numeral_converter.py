import pytest
from src.roman_numeral_converter import int_to_roman

def test_int_to_roman_standard_cases():
    # Test typical cases
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(27) == "XXVII"
    assert int_to_roman(49) == "XLIX"
    assert int_to_roman(99) == "XCIX"
    assert int_to_roman(500) == "D"
    assert int_to_roman(2023) == "MMXXIII"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_int_to_roman_boundary_cases():
    # Test boundary values
    assert int_to_roman(0) == ""
    assert int_to_roman(1) == "I"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_int_to_roman_invalid_inputs():
    # Test invalid inputs
    with pytest.raises(TypeError):
        int_to_roman("100")
    
    with pytest.raises(ValueError):
        int_to_roman(-1)
    
    with pytest.raises(ValueError):
        int_to_roman(4000)

def test_int_to_roman_intermediate_values():
    # Test some intermediate values
    assert int_to_roman(14) == "XIV"
    assert int_to_roman(89) == "LXXXIX"
    assert int_to_roman(444) == "CDXLIV"
    assert int_to_roman(1984) == "MCMLXXXIV"