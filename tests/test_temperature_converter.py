import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    """Test conversion of positive temperatures"""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_negative():
    """Test conversion of negative temperatures"""
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-100) == -148

def test_celsius_to_fahrenheit_decimal():
    """Test conversion of decimal temperatures"""
    assert round(celsius_to_fahrenheit(20.5), 2) == 68.9

def test_celsius_to_fahrenheit_type_error():
    """Test that TypeError is raised for invalid input types"""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)

def test_celsius_to_fahrenheit_edge_cases():
    """Test edge cases like zero and very large/small numbers"""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(float('inf')) == float('inf')
    assert celsius_to_fahrenheit(float('-inf')) == float('-inf')