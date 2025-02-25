import pytest
from src.roman_numeral_converter import int_to_roman

def test_basic_roman_numeral_conversions():
    """Test basic Roman numeral conversions"""
    assert int_to_roman(1) == 'I'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(27) == 'XXVII'
    assert int_to_roman(49) == 'XLIX'
    assert int_to_roman(99) == 'XCIX'
    assert int_to_roman(500) == 'D'
    assert int_to_roman(2023) == 'MMXXIII'
    assert int_to_roman(3999) == 'MMMCMXCIX'

def test_zero_conversion():
    """Test conversion of zero"""
    assert int_to_roman(0) == ''

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(4000)

def test_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman(3.14)