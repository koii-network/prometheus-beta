import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_lcm_recursive_basic():
    """Test basic LCM calculations"""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(12, 18) == 36

def test_lcm_recursive_prime_numbers():
    """Test LCM with prime numbers"""
    assert lcm_recursive(2, 3) == 6
    assert lcm_recursive(5, 7) == 35
    assert lcm_recursive(11, 13) == 143

def test_lcm_recursive_equal_numbers():
    """Test LCM when both numbers are the same"""
    assert lcm_recursive(7, 7) == 7
    assert lcm_recursive(13, 13) == 13

def test_gcd_recursive_validation():
    """Test the underlying GCD recursive function"""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1

def test_lcm_recursive_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        lcm_recursive(4.5, 6)
    
    with pytest.raises(TypeError):
        lcm_recursive("4", 6)
    
    with pytest.raises(ValueError):
        lcm_recursive(0, 6)
    
    with pytest.raises(ValueError):
        lcm_recursive(4, -6)
    
    with pytest.raises(ValueError):
        lcm_recursive(-4, -6)