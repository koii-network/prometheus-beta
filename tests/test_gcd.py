import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    """Test GCD for positive integers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_with_zero():
    """Test GCD with zero"""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_gcd_same_numbers():
    """Test GCD with identical numbers"""
    assert find_gcd(7, 7) == 7
    assert find_gcd(0, 0) == 0

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_gcd(4.5, 3)
    
    with pytest.raises(TypeError):
        find_gcd("10", 5)