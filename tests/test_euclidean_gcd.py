import pytest
from src.euclidean_gcd import euclidean_gcd

def test_euclidean_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1  # coprime numbers

def test_euclidean_gcd_one_zero():
    """Test GCD when one number is zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5

def test_euclidean_gcd_both_zero():
    """Test GCD when both numbers are zero"""
    assert euclidean_gcd(0, 0) == 0

def test_euclidean_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert euclidean_gcd(-48, 18) == 6
    assert euclidean_gcd(48, -18) == 6
    assert euclidean_gcd(-48, -18) == 6

def test_euclidean_gcd_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        euclidean_gcd(3.14, 5)
    with pytest.raises(ValueError):
        euclidean_gcd("10", 5)
    with pytest.raises(ValueError):
        euclidean_gcd([1], 5)