import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    assert fahrenheit_to_celsius(212) == 100

def test_zero_fahrenheit():
    assert fahrenheit_to_celsius(0) == -17.78

def test_negative_value():
    assert fahrenheit_to_celsius(-40) == -40

def test_float_input():
    assert fahrenheit_to_celsius(98.6) == 37

def test_invalid_input_type():
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")

def test_invalid_input_non_numeric():
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)