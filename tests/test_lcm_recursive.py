import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive():
    # Test basic GCD calculations
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5

def test_lcm_recursive():
    # Test basic LCM calculations
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(15, 25) == 75
    assert lcm_recursive(12, 18) == 36
    assert lcm_recursive(5, 7) == 35
    assert lcm_recursive(2, 3) == 6

def test_lcm_recursive_coprime():
    # Test LCM of coprime numbers
    assert lcm_recursive(17, 23) == 391
    assert lcm_recursive(11, 13) == 143

def test_lcm_recursive_same_number():
    # Test LCM when both numbers are the same
    assert lcm_recursive(5, 5) == 5
    assert lcm_recursive(7, 7) == 7

def test_lcm_recursive_invalid_input():
    # Test error handling for invalid inputs
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(5, 0)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(-3, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(4, -3)