import pytest
from src.simple_calculator import simple_calculator

def test_addition():
    assert simple_calculator(5, 3, '+') == 8
    assert simple_calculator(-2, 2, '+') == 0
    assert simple_calculator(1.5, 2.5, '+') == 4.0

def test_subtraction():
    assert simple_calculator(10, 4, '-') == 6
    assert simple_calculator(-5, -3, '-') == -2
    assert simple_calculator(5.5, 2.5, '-') == 3.0

def test_multiplication():
    assert simple_calculator(5, 3, '*') == 15
    assert simple_calculator(-2, 3, '*') == -6
    assert simple_calculator(1.5, 2, '*') == 3.0

def test_division():
    assert simple_calculator(10, 2, '/') == 5
    assert simple_calculator(-6, 3, '/') == -2
    assert simple_calculator(5.0, 2, '/') == 2.5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        simple_calculator(10, 0, '/')

def test_invalid_operator():
    with pytest.raises(ValueError, match="Invalid operator"):
        simple_calculator(5, 3, '%')

def test_invalid_input_type():
    with pytest.raises(ValueError):
        simple_calculator('a', 3, '+')