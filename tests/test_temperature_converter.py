import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_freezing_point():
    """Test the freezing point of water (0°C = 32°F)"""
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    """Test the boiling point of water (100°C = 212°F)"""
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    """Test a negative temperature conversion"""
    assert celsius_to_fahrenheit(-40) == -40

def test_fractional_temperature():
    """Test conversion of a fractional temperature"""
    assert abs(celsius_to_fahrenheit(37.5) - 99.5) < 0.001

def test_invalid_input_type():
    """Test that non-numeric input raises a TypeError"""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")