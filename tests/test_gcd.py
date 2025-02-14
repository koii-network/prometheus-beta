import pytest
from src.gcd import find_gcd

def test_positive_numbers():
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_one_zero():
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5

def test_both_zero():
    assert find_gcd(0, 0) == 0

def test_negative_numbers():
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_large_numbers():
    assert find_gcd(1071, 462) == 21

def test_invalid_input():
    with pytest.raises(ValueError):
        find_gcd(3.14, 5)
    
    with pytest.raises(ValueError):
        find_gcd("10", 5)
    
    with pytest.raises(ValueError):
        find_gcd([10], 5)