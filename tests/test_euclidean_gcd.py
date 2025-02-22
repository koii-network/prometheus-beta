import pytest
from src.euclidean_gcd import euclidean_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_one_zero():
    """Test GCD when one number is zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD of a number with itself"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_negative_inputs():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError):
        euclidean_gcd(-5, 10)
    with pytest.raises(ValueError):
        euclidean_gcd(5, -10)
    with pytest.raises(ValueError):
        euclidean_gcd(-5, -10)

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert euclidean_gcd(1071, 462) == 21
    assert euclidean_gcd(463, 1071) == 21