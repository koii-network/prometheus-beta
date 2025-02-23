import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of water's freezing point."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of water's boiling point."""
    assert round(fahrenheit_to_celsius(212), 2) == 100

def test_zero_fahrenheit():
    """Test conversion of zero Fahrenheit."""
    assert round(fahrenheit_to_celsius(0), 2) == -17.78

def test_negative_temperature():
    """Test conversion of a negative temperature."""
    assert round(fahrenheit_to_celsius(-40), 2) == -40

def test_raises_type_error_for_non_numeric():
    """Test that TypeError is raised for non-numeric input."""
    with pytest.raises(TypeError, match="Input must be a numeric value"):
        fahrenheit_to_celsius("not a number")

def test_float_input():
    """Test conversion with float input."""
    assert round(fahrenheit_to_celsius(98.6), 2) == 37