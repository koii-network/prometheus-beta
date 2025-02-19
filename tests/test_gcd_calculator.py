import pytest
from src.gcd_calculator import calculate_gcd

def test_gcd_basic_cases():
    """Test common GCD scenarios"""
    assert calculate_gcd(48, 18) == 6  # Known GCD
    assert calculate_gcd(54, 24) == 6  # Another known GCD
    assert calculate_gcd(17, 23) == 1  # Coprime numbers
    
def test_gcd_swapped_arguments():
    """Verify GCD is symmetric"""
    assert calculate_gcd(18, 48) == 6
    assert calculate_gcd(24, 54) == 6

def test_gcd_same_number():
    """Test when both numbers are the same"""
    assert calculate_gcd(7, 7) == 7
    assert calculate_gcd(100, 100) == 100

def test_gcd_one_number_is_multiple():
    """Test when one number is a multiple of the other"""
    assert calculate_gcd(12, 36) == 12
    assert calculate_gcd(36, 12) == 12

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd(10.5, 20)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(0, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(10, 0)