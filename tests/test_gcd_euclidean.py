import pytest
from src.gcd_euclidean import gcd_euclidean

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert gcd_euclidean(48, 18) == 6
    assert gcd_euclidean(54, 24) == 6
    assert gcd_euclidean(17, 23) == 1

def test_gcd_one_zero():
    """Test GCD with one zero input"""
    assert gcd_euclidean(0, 5) == 5
    assert gcd_euclidean(5, 0) == 5

def test_gcd_both_zero():
    """Test GCD when both inputs are zero"""
    assert gcd_euclidean(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert gcd_euclidean(-48, 18) == 6
    assert gcd_euclidean(48, -18) == 6
    assert gcd_euclidean(-48, -18) == 6

def test_gcd_invalid_inputs():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        gcd_euclidean(3.14, 5)
    with pytest.raises(ValueError):
        gcd_euclidean("10", 5)
    with pytest.raises(ValueError):
        gcd_euclidean([1, 2], 5)