import pytest
from src.lcm_calculator import calculate_lcm

def test_basic_lcm():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_same_number_lcm():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7
    assert calculate_lcm(11, 11) == 11

def test_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(3, 9) == 9
    assert calculate_lcm(8, 16) == 16

def test_prime_numbers():
    """Test LCM for prime numbers"""
    assert calculate_lcm(2, 3) == 6
    assert calculate_lcm(5, 7) == 35

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Both inputs must be integers"):
        calculate_lcm(4.5, 6)
        calculate_lcm("4", 6)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(0, 6)
        calculate_lcm(4, -3)
        calculate_lcm(-4, 6)
        calculate_lcm(0, 0)