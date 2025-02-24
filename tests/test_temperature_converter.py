import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    """Test conversion of a positive temperature."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_negative():
    """Test conversion of a negative temperature."""
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-273.15) == -459.67

def test_celsius_to_fahrenheit_floating_point():
    """Test conversion with floating point numbers."""
    assert round(celsius_to_fahrenheit(23.5), 1) == 74.3

def test_celsius_to_fahrenheit_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([1, 2, 3])