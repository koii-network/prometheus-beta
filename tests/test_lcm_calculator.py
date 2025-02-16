import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_numbers():
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(15, 25) == 75
    assert calculate_lcm(8, 12) == 24

def test_lcm_coprime_numbers():
    assert calculate_lcm(7, 13) == 91
    assert calculate_lcm(5, 17) == 85

def test_lcm_one_number_multiple_of_other():
    assert calculate_lcm(5, 10) == 10
    assert calculate_lcm(3, 9) == 9

def test_lcm_same_number():
    assert calculate_lcm(7, 7) == 7

def test_lcm_invalid_inputs():
    with pytest.raises(ValueError, match="Both inputs must be integers"):
        calculate_lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(-3, 5)
        
def test_lcm_large_numbers():
    assert calculate_lcm(1000, 1500) == 3000