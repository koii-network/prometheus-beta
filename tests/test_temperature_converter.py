import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_known_conversions():
    """Test known Fahrenheit to Celsius conversions"""
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(98.6) == 37

def test_negative_temperatures():
    """Test negative temperature conversions"""
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(-32) == -35.56

def test_float_input():
    """Test floating point conversions"""
    assert fahrenheit_to_celsius(68.5) == 20.28

def test_invalid_input_type():
    """Test input type validation"""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)