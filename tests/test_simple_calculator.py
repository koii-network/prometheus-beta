import pytest
from src.simple_calculator import simple_calculator

def test_addition():
    assert simple_calculator(5, 3, '+') == 8
    assert simple_calculator(-2, 4, '+') == 2
    assert simple_calculator(2.5, 3.5, '+') == 6.0

def test_subtraction():
    assert simple_calculator(10, 4, '-') == 6
    assert simple_calculator(-5, -3, '-') == -2
    assert simple_calculator(7.5, 2.5, '-') == 5.0

def test_multiplication():
    assert simple_calculator(5, 3, '*') == 15
    assert simple_calculator(-2, 4, '*') == -8
    assert simple_calculator(2.5, 2, '*') == 5.0

def test_division():
    assert simple_calculator(10, 2, '/') == 5
    assert simple_calculator(-6, 3, '/') == -2
    assert simple_calculator(7.5, 2.5, '/') == 3.0

def test_invalid_operator():
    with pytest.raises(ValueError, match="Invalid operator"):
        simple_calculator(5, 3, '%')

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        simple_calculator(10, 0, '/')

def test_string_inputs():
    assert simple_calculator('5', '3', '+') == 8
    assert simple_calculator('2.5', '3.5', '*') == 8.75