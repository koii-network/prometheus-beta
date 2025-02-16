import pytest
from src.euclidean_gcd import euclidean_gcd

def test_gcd_positive_numbers():
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_zero_cases():
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_negative_numbers():
    assert euclidean_gcd(-48, 18) == 6
    assert euclidean_gcd(48, -18) == 6
    assert euclidean_gcd(-48, -18) == 6

def test_gcd_same_number():
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_one():
    assert euclidean_gcd(1, 5) == 1
    assert euclidean_gcd(5, 1) == 1

def test_invalid_inputs():
    with pytest.raises(ValueError):
        euclidean_gcd('a', 5)
    with pytest.raises(ValueError):
        euclidean_gcd(5, '10')
    with pytest.raises(ValueError):
        euclidean_gcd(5.5, 10)
    with pytest.raises(ValueError):
        euclidean_gcd(None, 10)