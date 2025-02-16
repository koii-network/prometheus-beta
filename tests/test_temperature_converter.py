import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    assert fahrenheit_to_celsius(212) == 100

def test_negative_temperature():
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_temperature():
    assert fahrenheit_to_celsius(98.6) == 37

def test_error_handling():
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")
    
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)