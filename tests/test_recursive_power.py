import pytest
from src.recursive_power import recursive_power

def test_recursive_power_positive_cases():
    assert recursive_power(2, 3) == 8
    assert recursive_power(5, 2) == 25
    assert recursive_power(10, 0) == 1
    assert recursive_power(3, 1) == 3

def test_recursive_power_zero_base():
    assert recursive_power(0, 5) == 0
    assert recursive_power(0, 0) == 1

def test_recursive_power_float_base():
    assert recursive_power(2.5, 2) == 6.25
    pytest.approx(recursive_power(1.5, 3), 3.375)

def test_recursive_power_negative_exponent():
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        recursive_power(2, -1)

def test_recursive_power_invalid_exponent_type():
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 3.5)
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, "2")