import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    """Test conversion of a positive Celsius temperature"""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_negative():
    """Test conversion of a negative Celsius temperature"""
    assert celsius_to_fahrenheit(-40) == -40.0
    assert celsius_to_fahrenheit(-273.15) == -459.67

def test_celsius_to_fahrenheit_decimal():
    """Test conversion of decimal temperatures"""
    assert round(celsius_to_fahrenheit(25.5), 2) == 77.9

def test_celsius_to_fahrenheit_invalid_input():
    """Test that invalid input raises a TypeError"""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([])