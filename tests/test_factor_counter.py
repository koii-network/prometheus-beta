import pytest
from src.factor_counter import count_factors

def test_prime_number_has_two_factors():
    assert count_factors(7) == 2

def test_square_number_factors():
    assert count_factors(9) == 3  # 1, 3, 9

def test_composite_number_factors():
    assert count_factors(12) == 6  # 1, 2, 3, 4, 6, 12

def test_number_one_has_one_factor():
    assert count_factors(1) == 1

def test_invalid_input_negative():
    with pytest.raises(ValueError):
        count_factors(-5)

def test_invalid_input_zero():
    with pytest.raises(ValueError):
        count_factors(0)

def test_invalid_input_float():
    with pytest.raises(ValueError):
        count_factors(3.14)

def test_invalid_input_string():
    with pytest.raises(ValueError):
        count_factors("12")