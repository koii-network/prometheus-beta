import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_fahrenheit_float():
    assert round(celsius_to_fahrenheit(37.5), 1) == 99.5

def test_celsius_to_fahrenheit_type_error():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)