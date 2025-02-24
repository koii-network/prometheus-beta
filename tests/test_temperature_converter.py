import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_known_conversions():
    """Test specific known Celsius to Fahrenheit conversions."""
    # Freezing point of water
    assert abs(celsius_to_fahrenheit(0) - 32) < 0.001
    
    # Boiling point of water
    assert abs(celsius_to_fahrenheit(100) - 212) < 0.001
    
    # Negative temperature
    assert abs(celsius_to_fahrenheit(-40) - (-40)) < 0.001

def test_float_conversions():
    """Test conversion with float values."""
    assert abs(celsius_to_fahrenheit(37.5) - 99.5) < 0.001
    assert abs(celsius_to_fahrenheit(-17.8) - 0.04) < 0.01

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Test non-numeric input
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([])

def test_integer_conversion():
    """Ensure integer inputs work correctly."""
    assert abs(celsius_to_fahrenheit(20) - 68) < 0.001
    assert abs(celsius_to_fahrenheit(-10) - 14) < 0.001