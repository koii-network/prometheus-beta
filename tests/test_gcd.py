import pytest
from src.gcd import find_gcd

def test_gcd_basic_cases():
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_same_number():
    assert find_gcd(7, 7) == 7
    assert find_gcd(100, 100) == 100

def test_gcd_one_divides_other():
    assert find_gcd(12, 4) == 4
    assert find_gcd(21, 3) == 3

def test_gcd_coprime_numbers():
    assert find_gcd(17, 23) == 1
    assert find_gcd(13, 11) == 1

def test_gcd_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_gcd(1.5, 2)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(-10, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(10, 0)
        
def test_gcd_order_independence():
    assert find_gcd(48, 18) == find_gcd(18, 48)