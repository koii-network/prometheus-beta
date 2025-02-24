import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of water's freezing point (32°F)."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of water's boiling point (212°F)."""
    assert fahrenheit_to_celsius(212) == 100

def test_negative_temperature():
    """Test conversion of a negative temperature."""
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_temperature():
    """Test conversion of a decimal temperature."""
    assert fahrenheit_to_celsius(98.6) == 37

def test_large_temperature():
    """Test conversion of a large temperature."""
    assert fahrenheit_to_celsius(1000) == 537.78

def test_invalid_input_type():
    """Test that TypeError is raised for non-numeric input."""
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius("not a number")

def test_invalid_input_none():
    """Test that TypeError is raised for None input."""
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius(None)