import pytest
from src.gcd import euclidean_gcd

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_zero():
    """Test GCD with zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD of a number with itself"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(13, 13) == 13

def test_gcd_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-5, 10)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(5, -10)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-5, -10)

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert euclidean_gcd(1071, 462) == 21
    assert euclidean_gcd(123456, 789012) == 12  # Corrected the expected GCD