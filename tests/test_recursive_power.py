import pytest
from src.recursive_power import calculate_power

def test_power_zero_exponent():
    """Test power calculation with zero exponent"""
    assert calculate_power(5, 0) == 1
    assert calculate_power(2.5, 0) == 1

def test_power_first_exponent():
    """Test power calculation with first power"""
    assert calculate_power(5, 1) == 5
    assert calculate_power(2.5, 1) == 2.5

def test_power_positive_exponent():
    """Test power calculation with positive exponents"""
    assert calculate_power(2, 3) == 8
    assert calculate_power(3, 4) == 81
    assert calculate_power(2.5, 2) == 6.25

def test_power_invalid_exponent_type():
    """Test that TypeError is raised for non-integer exponents"""
    with pytest.raises(TypeError):
        calculate_power(2, 3.5)
    with pytest.raises(TypeError):
        calculate_power(2, '2')

def test_power_negative_exponent():
    """Test that ValueError is raised for negative exponents"""
    with pytest.raises(ValueError):
        calculate_power(2, -1)