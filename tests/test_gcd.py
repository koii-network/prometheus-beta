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

def test_gcd_negative_inputs():
    """Test GCD with negative inputs"""
    assert euclidean_gcd(-48, 18) == 6
    assert euclidean_gcd(48, -18) == 6
    assert euclidean_gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD when both inputs are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_invalid_inputs():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        euclidean_gcd(3.14, 5)
    with pytest.raises(ValueError):
        euclidean_gcd('10', 5)
    with pytest.raises(ValueError):
        euclidean_gcd([10], 5)