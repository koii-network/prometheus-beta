import pytest
from src.recursive_power import recursive_power

def test_power_positive_integers():
    assert recursive_power(2, 3) == 8
    assert recursive_power(3, 4) == 81
    assert recursive_power(5, 0) == 1
    assert recursive_power(10, 1) == 10

def test_power_float_base():
    assert recursive_power(2.5, 2) == 6.25
    assert recursive_power(1.5, 3) == 3.375

def test_power_even_and_odd_exponents():
    assert recursive_power(2, 2) == 4  # Even exponent
    assert recursive_power(2, 3) == 8  # Odd exponent
    assert recursive_power(3, 4) == 81

def test_zero_base():
    assert recursive_power(0, 5) == 0
    assert recursive_power(0, 0) == 1

def test_one_base():
    assert recursive_power(1, 100) == 1

def test_negative_exponent_raises_error():
    with pytest.raises(ValueError, match="Exponent cannot be negative"):
        recursive_power(2, -3)

def test_non_integer_exponent_raises_error():
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 3.5)
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, "2")