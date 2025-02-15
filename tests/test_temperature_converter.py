import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_freezing_point():
    """Test conversion of 0°C to 32°F"""
    assert celsius_to_fahrenheit(0) == 32.0

def test_boiling_point():
    """Test conversion of 100°C to 212°F"""
    assert celsius_to_fahrenheit(100) == 212.0

def test_negative_temperature():
    """Test conversion of a negative temperature"""
    assert celsius_to_fahrenheit(-40) == -40.0

def test_decimal_temperature():
    """Test conversion of a decimal temperature"""
    assert round(celsius_to_fahrenheit(37.5), 1) == 99.5

def test_invalid_input_type():
    """Test that TypeError is raised for non-numeric input"""
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_fahrenheit(None)