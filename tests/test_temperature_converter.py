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
    assert celsius_to_fahrenheit(-10) == 14

def test_celsius_to_fahrenheit_float():
    """Test conversion of floating point temperatures."""
    assert abs(celsius_to_fahrenheit(23.5) - 74.3) < 0.1

def test_celsius_to_fahrenheit_type_error():
    """Test that TypeError is raised for non-numeric inputs."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([])

def test_celsius_to_fahrenheit_zero():
    """Test conversion of zero."""
    assert celsius_to_fahrenheit(0) == 32