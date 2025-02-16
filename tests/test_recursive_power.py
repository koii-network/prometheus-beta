import pytest
from src.recursive_power import recursive_power

def test_positive_integer_power():
    assert recursive_power(2, 3) == 8
    assert recursive_power(5, 2) == 25
    assert recursive_power(10, 0) == 1

def test_float_base():
    assert recursive_power(2.5, 2) == 6.25
    assert recursive_power(1.5, 3) == 3.375

def test_zero_base():
    assert recursive_power(0, 5) == 0
    assert recursive_power(0, 0) == 1

def test_negative_exponent_raises_error():
    with pytest.raises(ValueError):
        recursive_power(2, -1)

def test_invalid_type_raises_error():
    with pytest.raises(TypeError):
        recursive_power("2", 3)
    with pytest.raises(TypeError):
        recursive_power(2, "3")
    with pytest.raises(TypeError):
        recursive_power([], 3)