import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_one_zero():
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5
    assert find_gcd(0, 0) == 0

def test_gcd_negative_numbers():
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_gcd_same_number():
    assert find_gcd(7, 7) == 7
    assert find_gcd(100, 100) == 100

def test_gcd_invalid_input():
    with pytest.raises(ValueError):
        find_gcd(3.5, 4)
    with pytest.raises(ValueError):
        find_gcd("10", 5)
    with pytest.raises(ValueError):
        find_gcd([10], 5)