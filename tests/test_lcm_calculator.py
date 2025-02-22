import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_numbers():
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(15, 25) == 75
    assert calculate_lcm(12, 18) == 36

def test_lcm_one_number_is_one():
    assert calculate_lcm(1, 5) == 5
    assert calculate_lcm(7, 1) == 7

def test_lcm_same_numbers():
    assert calculate_lcm(7, 7) == 7
    assert calculate_lcm(11, 11) == 11

def test_lcm_prime_numbers():
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_lcm_large_numbers():
    assert calculate_lcm(100, 200) == 200

def test_lcm_zero_or_negative_numbers():
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-3, 4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(6, -2)

def test_lcm_non_integer_inputs():
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(3.5, 4)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(5, "10")
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm([2], 3)