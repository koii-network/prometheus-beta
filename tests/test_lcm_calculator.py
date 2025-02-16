import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_cases():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_number_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(4, 8) == 8
    assert calculate_lcm(8, 4) == 8

def test_lcm_prime_numbers():
    """Test LCM with prime numbers"""
    assert calculate_lcm(11, 13) == 143

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(4.5, 6)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm("4", 6)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 6)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(4, -6)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-4, -6)