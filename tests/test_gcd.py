import pytest
from src.gcd import recursive_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 23) == 1
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(0, 0) == 0

def test_gcd_one_zero():
    """Test GCD with one number being zero"""
    assert recursive_gcd(0, 0) == 0

def test_gcd_error_handling():
    """Test error handling for invalid inputs"""
    # Negative input should raise ValueError
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(-5, 10)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(5, -10)
    
    # Non-integer input should raise TypeError
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(5.5, 10)
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(5, "10")
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd([5], 10)