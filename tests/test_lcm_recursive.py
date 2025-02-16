import pytest
from src.lcm_recursive import calculate_lcm_recursive

def test_lcm_basic_cases():
    assert calculate_lcm_recursive(4, 6) == 12
    assert calculate_lcm_recursive(21, 6) == 42
    assert calculate_lcm_recursive(3, 5) == 15

def test_lcm_same_number():
    assert calculate_lcm_recursive(7, 7) == 7

def test_lcm_coprime():
    assert calculate_lcm_recursive(17, 23) == 391

def test_lcm_one_divides_other():
    assert calculate_lcm_recursive(5, 15) == 15
    assert calculate_lcm_recursive(15, 5) == 15

def test_lcm_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm_recursive(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm_recursive(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm_recursive(-3, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm_recursive(3, -4)