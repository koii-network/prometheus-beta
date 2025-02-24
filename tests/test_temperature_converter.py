import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of freezing point (32°F = 0°C)"""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of boiling point (212°F = 100°C)"""
    assert fahrenheit_to_celsius(212) == 100

def test_negative_temperature():
    """Test conversion of a negative temperature"""
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_temperature():
    """Test conversion of a decimal temperature"""
    assert fahrenheit_to_celsius(98.6) == 37

def test_zero_fahrenheit():
    """Test conversion of 0°F"""
    assert fahrenheit_to_celsius(0) == -17.78

def test_type_error_for_string():
    """Test that a TypeError is raised for string input"""
    with pytest.raises(TypeError, match="Input must be a numeric value"):
        fahrenheit_to_celsius("not a number")

def test_type_error_for_none():
    """Test that a TypeError is raised for None input"""
    with pytest.raises(TypeError, match="Input must be a numeric value"):
        fahrenheit_to_celsius(None)

def test_large_number():
    """Test conversion of a large temperature value"""
    assert fahrenheit_to_celsius(1000) == 537.78