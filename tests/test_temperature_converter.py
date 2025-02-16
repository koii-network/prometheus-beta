import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40

def test_fractional_temperature():
    assert round(celsius_to_fahrenheit(37.5), 2) == 99.5

def test_invalid_input_type():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")

def test_invalid_input_list():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([1, 2, 3])