import pytest
from src.gcd import euclidean_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_zero_cases():
    """Test cases involving zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_one_is_multiple():
    """Test GCD when one number is a multiple of the other"""
    assert euclidean_gcd(12, 3) == 3
    assert euclidean_gcd(3, 12) == 3

def test_gcd_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(5, -10)
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd(5.5, 10)
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd(5, "10")