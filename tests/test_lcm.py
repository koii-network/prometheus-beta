import pytest
from src.lcm import find_lcm

def test_basic_lcm():
    """Test basic LCM calculations"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_same_number_lcm():
    """Test LCM with identical numbers"""
    assert find_lcm(7, 7) == 7
    assert find_lcm(10, 10) == 10

def test_one_and_another_number():
    """Test LCM with 1 and another number"""
    assert find_lcm(1, 15) == 15
    assert find_lcm(15, 1) == 15

def test_prime_numbers():
    """Test LCM with prime numbers"""
    assert find_lcm(11, 13) == 143
    assert find_lcm(2, 3) == 6

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        find_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        find_lcm(5, 0)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        find_lcm(-4, 6)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        find_lcm(6, -4)