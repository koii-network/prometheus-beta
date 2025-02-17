import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_zero_celsius():
    """Test converting 0°C to Fahrenheit"""
    assert celsius_to_fahrenheit(0) == 32

def test_positive_celsius():
    """Test converting a positive Celsius value"""
    assert celsius_to_fahrenheit(100) == 212

def test_negative_celsius():
    """Test converting a negative Celsius value"""
    assert celsius_to_fahrenheit(-40) == -40

def test_float_celsius():
    """Test converting a float Celsius value"""
    assert celsius_to_fahrenheit(37.5) == 99.5

def test_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([1, 2, 3])