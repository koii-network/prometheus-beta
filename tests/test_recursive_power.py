import pytest
from src.recursive_power import recursive_power

def test_recursive_power_positive_integers():
    assert recursive_power(2, 3) == 8
    assert recursive_power(3, 4) == 81
    assert recursive_power(5, 0) == 1

def test_recursive_power_base_1():
    assert recursive_power(1, 10) == 1

def test_recursive_power_exponent_1():
    assert recursive_power(7, 1) == 7

def test_recursive_power_zero_base():
    assert recursive_power(0, 5) == 0
    assert recursive_power(0, 0) == 1

def test_recursive_power_float_base():
    assert recursive_power(2.5, 2) == 6.25
    pytest.approx(recursive_power(1.5, 3), 3.375)

def test_recursive_power_negative_exponent():
    with pytest.raises(ValueError, match="Exponent must be a non-negative integer"):
        recursive_power(2, -1)