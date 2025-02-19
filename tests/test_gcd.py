import pytest
from src.gcd import calculate_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert calculate_gcd(48, 18) == 6
    assert calculate_gcd(54, 24) == 6
    assert calculate_gcd(17, 23) == 1  # Coprime numbers
    assert calculate_gcd(100, 75) == 25

def test_gcd_equal_numbers():
    """Test when both numbers are equal"""
    assert calculate_gcd(7, 7) == 7
    assert calculate_gcd(13, 13) == 13

def test_gcd_one_is_multiple():
    """Test when one number is a multiple of the other"""
    assert calculate_gcd(15, 5) == 5
    assert calculate_gcd(21, 7) == 7

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Negative numbers
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(-10, 20)
    
    # Zero input
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(0, 5)
    
    # Non-integer inputs
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd(10.5, 20)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd("10", 20)