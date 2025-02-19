import pytest
from src.roman_numeral_converter import int_to_roman

def test_int_to_roman_zero():
    """Test conversion of 0"""
    assert int_to_roman(0) == ""

def test_int_to_roman_ones():
    """Test numbers 1-9"""
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"

def test_int_to_roman_tens():
    """Test numbers 10-99"""
    assert int_to_roman(10) == "X"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(49) == "XLIX"
    assert int_to_roman(99) == "XCIX"

def test_int_to_roman_hundreds():
    """Test numbers 100-999"""
    assert int_to_roman(100) == "C"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(499) == "CDXCIX"
    assert int_to_roman(999) == "CMXCIX"

def test_int_to_roman_thousands():
    """Test numbers 1000-3999"""
    assert int_to_roman(1000) == "M"
    assert int_to_roman(1954) == "MCMLIV"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_int_to_roman_invalid_input():
    """Test invalid inputs"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        int_to_roman("100")
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(4000)