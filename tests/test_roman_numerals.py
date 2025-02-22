import pytest
from src.roman_numerals import convert_to_roman_numeral

def test_basic_roman_numeral_conversion():
    """Test basic Roman numeral conversions."""
    test_cases = [
        (1, 'I'),
        (4, 'IV'),
        (9, 'IX'),
        (14, 'XIV'),
        (49, 'XLIX'),
        (99, 'XCIX'),
        (500, 'D'),
        (678, 'DCLXXVIII'),
        (999, 'CMXCIX'),
        (2023, 'MMXXIII'),
        (3888, 'MMMDCCCLXXXVIII'),
        (3999, 'MMMCMXCIX')
    ]
    
    for number, expected in test_cases:
        assert convert_to_roman_numeral(number) == expected, f"Failed for {number}"

def test_zero_input():
    """Test that zero returns an empty string."""
    assert convert_to_roman_numeral(0) == ""

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman_numeral(-1)
    
    # Test numbers above 3999
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman_numeral(4000)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman_numeral(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman_numeral("42")